#Бинарная куча
class MaxHeap:
    def __init__(self):
        self.data = []

    def _parent(self, idx):
        return (idx - 1) // 2

    def _left(self, idx):
        return 2 * idx + 1

    def _right(self, idx):
        return 2 * idx + 2

    def add(self, val):
        self.data.append(val)
        self._bubble_up(len(self.data) - 1)

    def _bubble_up(self, idx):
        while idx > 0 and self.data[self._parent(idx)] < self.data[idx]:
            self.data[self._parent(idx)], self.data[idx] = self.data[idx], self.data[self._parent(idx)]
            idx = self._parent(idx)

    def pop_max(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        max_val = self.data[0]
        self.data[0] = self.data.pop()
        self._bubble_down(0)
        return max_val

    def _bubble_down(self, idx):
        largest = idx
        left = self._left(idx)
        right = self._right(idx)
        size = len(self.data)

        if left < size and self.data[left] > self.data[largest]:
            largest = left
        if right < size and self.data[right] > self.data[largest]:
            largest = right
        if largest != idx:
            self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
            self._bubble_down(largest)

    def peek(self):
        return self.data[0] if self.data else None

    def length(self):
        return len(self.data)


# Пример использования
heap = MaxHeap()
heap.add(12)
heap.add(7)
heap.add(25)
print("Максимум:", heap.peek())        # 25
print("Извлечь максимум:", heap.pop_max())  # 25
print("Максимум после извлечения:", heap.peek())  # 12

################################################################################
#Биномиальная куча
class BNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.sibling = None
        self.degree = 0

class BHeap:
    def __init__(self):
        self.head = None

    def _merge_heads(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.degree <= h2.degree:
            res = h1
            res.sibling = self._merge_heads(h1.sibling, h2)
        else:
            res = h2
            res.sibling = self._merge_heads(h1, h2.sibling)
        return res

    def _link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def _union(self, other):
        new_heap = BHeap()
        new_heap.head = self._merge_heads(self.head, other.head)
        if new_heap.head is None:
            return new_heap

        prev = None
        curr = new_heap.head
        next = curr.sibling

        while next:
            if (curr.degree != next.degree) or (next.sibling and next.sibling.degree == curr.degree):
                prev = curr
                curr = next
            else:
                if curr.key <= next.key:
                    curr.sibling = next.sibling
                    self._link(next, curr)
                else:
                    if prev is None:
                        new_heap.head = next
                    else:
                        prev.sibling = next
                    self._link(curr, next)
                    curr = next
            next = curr.sibling
        return new_heap

    def insert(self, key):
        new_node = BNode(key)
        temp_heap = BHeap()
        temp_heap.head = new_node
        self.head = self._union(temp_heap).head

    def find_min(self):
        if not self.head:
            return None
        curr = self.head
        min_node = curr
        min_key = curr.key
        while curr:
            if curr.key < min_key:
                min_node = curr
                min_key = curr.key
            curr = curr.sibling
        return min_key

    def extract_min(self):
        if not self.head:
            return None
        prev_min = None
        min_node = self.head
        prev = None
        curr = self.head
        min_key = curr.key
        while curr:
            if curr.key < min_key:
                min_key = curr.key
                prev_min = prev
                min_node = curr
            prev = curr
            curr = curr.sibling

        if prev_min is None:
            self.head = min_node.sibling
        else:
            prev_min.sibling = min_node.sibling

        child = min_node.child
        prev_child = None
        while child:
            next_child = child.sibling
            child.sibling = prev_child
            child.parent = None
            prev_child = child
            child = next_child

        new_heap = BHeap()
        new_heap.head = prev_child

        self.head = self._union(new_heap).head
        return min_key

# Пример использования
bh = BHeap()
bh.insert(15)
bh.insert(6)
bh.insert(23)
bh.insert(4)
bh.insert(9)

print("Минимальный элемент:", bh.find_min())  # 4
print("Удалён минимальный элемент:", bh.extract_min())  # 4
print("Новый минимальный элемент:", bh.find_min())  # 6

################################################################################
#Куча Фибоначчи
class FNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False

class FibHeap:
    def __init__(self):
        self.min = None
        self.count = 0

    def insert(self, key):
        node = FNode(key)
        if self.min is None:
            self.min = node
        else:
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            if key < self.min.key:
                self.min = node
        self.count += 1
        return node

    def merge(self, other):
        if other.min is None:
            return
        if self.min is None:
            self.min = other.min
            self.count = other.count
            return
        self.min.right.left = other.min.left
        other.min.left.right = self.min.right
        self.min.right = other.min
        other.min.left = self.min
        if other.min.key < self.min.key:
            self.min = other.min
        self.count += other.count

    def find_min(self):
        return self.min.key if self.min else None

# Пример использования
fh = FibHeap()
fh.insert(17)
fh.insert(8)
fh.insert(29)

print("Минимальный элемент в куче Фибоначчи:", fh.find_min())

#Хэш-таблица
class HashMap:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash_func(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        idx = self._hash_func(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash_func(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self._hash_func(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

# Пример работы с хеш-таблицей
hm = HashMap()
hm.set("orange", 15)
hm.set("melon", 30)
print(hm.get("orange"))  # 15
print(hm.get("melon"))   # 30
hm.remove("orange")
print(hm.get("orange"))  # None
