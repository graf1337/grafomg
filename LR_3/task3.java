#Бинарная куча
import java.util.ArrayList;

public class MaxHeap {
    private ArrayList<Integer> data;

    public MaxHeap() {
        data = new ArrayList<>();
    }

    private int parent(int i) {
        return (i - 1) / 2;
    }

    private int leftChild(int i) {
        return 2 * i + 1;
    }

    private int rightChild(int i) {
        return 2 * i + 2;
    }

    private void siftUp(int i) {
        while (i > 0 && data.get(parent(i)) < data.get(i)) {
            int temp = data.get(parent(i));
            data.set(parent(i), data.get(i));
            data.set(i, temp);
            i = parent(i);
        }
    }

    private void siftDown(int i) {
        int maxIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);
        if (left < data.size() && data.get(left) > data.get(maxIndex)) {
            maxIndex = left;
        }
        if (right < data.size() && data.get(right) > data.get(maxIndex)) {
            maxIndex = right;
        }
        if (i != maxIndex) {
            int temp = data.get(i);
            data.set(i, data.get(maxIndex));
            data.set(maxIndex, temp);
            siftDown(maxIndex);
        }
    }

    public void insert(int key) {
        data.add(key);
        siftUp(data.size() - 1);
    }

    public Integer extractMax() {
        if (data.isEmpty()) {
            return null;
        }
        int result = data.get(0);
        int last = data.remove(data.size() - 1);
        if (!data.isEmpty()) {
            data.set(0, last);
            siftDown(0);
        }
        return result;
    }

    public Integer getMax() {
        if (data.isEmpty()) {
            return null;
        }
        return data.get(0);
    }

    public int size() {
        return data.size();
    }

    // Пример использования
    public static void main(String[] args) {
        MaxHeap heap = new MaxHeap();
        heap.insert(30);
        heap.insert(10);
        heap.insert(50);
        System.out.println("Максимум: " + heap.getMax());
        System.out.println("Извлечь максимум: " + heap.extractMax());
        System.out.println("Максимум после извлечения: " + heap.getMax());
    }
}

#Биномиальная куча
class BNode {
    int key;
    int degree;
    BNode parent, child, sibling;

    BNode(int key) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.child = null;
        this.sibling = null;
    }
}

public class BinomialHeap {
    private BNode head;

    private BNode mergeRoots(BNode h1, BNode h2) {
        if (h1 == null) return h2;
        if (h2 == null) return h1;
        if (h1.degree <= h2.degree) {
            h1.sibling = mergeRoots(h1.sibling, h2);
            return h1;
        } else {
            h2.sibling = mergeRoots(h1, h2.sibling);
            return h2;
        }
    }

    private void linkTrees(BNode y, BNode z) {
        y.parent = z;
        y.sibling = z.child;
        z.child = y;
        z.degree++;
    }

    private BNode union(BNode h1, BNode h2) {
        BNode newHead = mergeRoots(h1, h2);
        if (newHead == null) return null;

        BNode prev = null;
        BNode curr = newHead;
        BNode next = curr.sibling;

        while (next != null) {
            if (curr.degree != next.degree ||
                (next.sibling != null && next.sibling.degree == curr.degree)) {
                prev = curr;
                curr = next;
            } else {
                if (curr.key <= next.key) {
                    curr.sibling = next.sibling;
                    linkTrees(next, curr);
                } else {
                    if (prev == null) {
                        newHead = next;
                    } else {
                        prev.sibling = next;
                    }
                    linkTrees(curr, next);
                    curr = next;
                }
            }
            next = curr.sibling;
        }

        return newHead;
    }

    public void insert(int key) {
        BNode newNode = new BNode(key);
        BinomialHeap tempHeap = new BinomialHeap();
        tempHeap.head = newNode;
        this.head = union(this.head, tempHeap.head);
    }

    public int findMin() {
        if (head == null) return Integer.MAX_VALUE;
        BNode curr = head;
        int minKey = curr.key;
        while (curr != null) {
            if (curr.key < minKey) minKey = curr.key;
            curr = curr.sibling;
        }
        return minKey;
    }

    // Можно добавить extractMin и другие методы
}

#Куча Фибоначчи
public class FNode {
    int key, degree;
    FNode parent, child, left, right;
    boolean mark;

    FNode(int key) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.child = null;
        this.left = this;
        this.right = this;
        this.mark = false;
    }
}

public class FibonacciHeap {
    private FNode min;
    private int size;

    public FibonacciHeap() {
        min = null;
        size = 0;
    }

    public void insert(int key) {
        FNode node = new FNode(key);
        if (min == null) {
            min = node;
        } else {
            // Вставляем в корневой список
            node.left = min;
            node.right = min.right;
            min.right.left = node;
            min.right = node;
            if (key < min.key) {
                min = node;
            }
        }
        size++;
    }

    public Integer findMin() {
        if (min == null) return null;
        return min.key;
    }

    // Другие методы: extractMin, decreaseKey и т.д.
}

#Хэш-таблицы
import java.util.LinkedList;

public class HashTable {
    private static class Entry {
        String key;
        int value;

        Entry(String key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity = 11;
    private LinkedList<Entry>[] table;

    @SuppressWarnings("unchecked")
    public HashTable() {
        table = new LinkedList[capacity];
        for (int i = 0; i < capacity; i++) {
            table[i] = new LinkedList<>();
        }
    }

    private int hash(String key) {
        return Math.abs(key.hashCode()) % capacity;
    }

    public void put(String key, int value) {
        int idx = hash(key);
        LinkedList<Entry> bucket = table[idx];
        for (Entry e : bucket) {
            if (e.key.equals(key)) {
                e.value = value;
                return;
            }
        }
        bucket.add(new Entry(key, value));
    }

    public Integer get(String key) {
        int idx = hash(key);
        for (Entry e : table[idx]) {
            if (e.key.equals(key)) {
                return e.value;
            }
        }
        return null;
    }

    public boolean remove(String key) {
        int idx = hash(key);
        LinkedList<Entry> bucket = table[idx];
        return bucket.removeIf(e -> e.key.equals(key));
    }
}
