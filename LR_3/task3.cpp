#Бинарная куча
#include <vector>
#include <iostream>

class MaxHeap {
    std::vector<int> data;

    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }

    void siftUp(int i) {
        while (i > 0 && data[parent(i)] < data[i]) {
            std::swap(data[parent(i)], data[i]);
            i = parent(i);
        }
    }

    void siftDown(int i) {
        int maxIndex = i;
        int l = leftChild(i);
        int r = rightChild(i);
        if (l < (int)data.size() && data[l] > data[maxIndex])
            maxIndex = l;
        if (r < (int)data.size() && data[r] > data[maxIndex])
            maxIndex = r;
        if (i != maxIndex) {
            std::swap(data[i], data[maxIndex]);
            siftDown(maxIndex);
        }
    }

public:
    void insert(int key) {
        data.push_back(key);
        siftUp((int)data.size() - 1);
    }

    int extractMax() {
        if (data.empty())
            return -1; // или выбросить исключение
        int maxVal = data[0];
        data[0] = data.back();
        data.pop_back();
        if (!data.empty())
            siftDown(0);
        return maxVal;
    }

    int getMax() {
        if (data.empty())
            return -1;
        return data[0];
    }

    int size() {
        return (int)data.size();
    }
};

// Пример использования
int main() {
    MaxHeap mh;
    mh.insert(12);
    mh.insert(7);
    mh.insert(25);
    std::cout << "Максимальный: " << mh.getMax() << std::endl;  // 25
    std::cout << "Извлечь максимум: " << mh.extractMax() << std::endl;  // 25
    std::cout << "Максимум после извлечения: " << mh.getMax() << std::endl;  // 12
}

#Биномиальная куча
struct BNode {
    int key;
    int degree;
    BNode* parent;
    BNode* child;
    BNode* sibling;

    BNode(int k) : key(k), degree(0), parent(nullptr), child(nullptr), sibling(nullptr) {}
};

class BHeap {
    BNode* head;

    BNode* mergeRoots(BNode* h1, BNode* h2) {
        if (!h1) return h2;
        if (!h2) return h1;
        if (h1->degree <= h2->degree) {
            h1->sibling = mergeRoots(h1->sibling, h2);
            return h1;
        } else {
            h2->sibling = mergeRoots(h1, h2->sibling);
            return h2;
        }
    }

    void linkTrees(BNode* y, BNode* z) {
        y->parent = z;
        y->sibling = z->child;
        z->child = y;
        z->degree++;
    }

public:
    BHeap() : head(nullptr) {}

    void insert(int key) {
        BNode* newNode = new BNode(key);
        BHeap tempHeap;
        tempHeap.head = newNode;
        head = unionHeap(tempHeap);
    }

    BNode* unionHeap(BHeap& other) {
        BNode* newHead = mergeRoots(head, other.head);
        if (!newHead) return nullptr;

        BNode* prev = nullptr;
        BNode* curr = newHead;
        BNode* next = curr->sibling;

        while (next != nullptr) {
            if (curr->degree != next->degree ||
                (next->sibling != nullptr && next->sibling->degree == curr->degree)) {
                prev = curr;
                curr = next;
            } else {
                if (curr->key <= next->key) {
                    curr->sibling = next->sibling;
                    linkTrees(next, curr);
                } else {
                    if (prev == nullptr) {
                        newHead = next;
                    } else {
                        prev->sibling = next;
                    }
                    linkTrees(curr, next);
                    curr = next;
                }
            }
            next = curr->sibling;
        }
        return newHead;
    }

    int findMin() {
        if (!head) return -1;
        BNode* curr = head;
        int minKey = curr->key;
        while (curr) {
            if (curr->key < minKey) minKey = curr->key;
            curr = curr->sibling;
        }
        return minKey;
    }
};

#Куча Фибоначчи
#include <iostream>

struct FNode {
    int key;
    int degree;
    FNode* parent;
    FNode* child;
    FNode* left;
    FNode* right;
    bool mark;

    FNode(int k) : key(k), degree(0), parent(nullptr), child(nullptr), mark(false) {
        left = right = this;
    }
};

class FibHeap {
    FNode* minNode;
    int n;

public:
    FibHeap() : minNode(nullptr), n(0) {}

    void insert(int key) {
        FNode* node = new FNode(key);
        if (!minNode) {
            minNode = node;
        } else {
            node->left = minNode;
            node->right = minNode->right;
            minNode->right->left = node;
            minNode->right = node;
            if (key < minNode->key) minNode = node;
        }
        n++;
    }

    int findMin() {
        return minNode ? minNode->key : -1;
    }
};

// Пример использования
int main() {
    FibHeap fh;
    fh.insert(30);
    fh.insert(10);
    fh.insert(20);
    std::cout << "Минимальный ключ: " << fh.findMin() << std::endl;  // 10
}

#Хэш-таблица
#include <iostream>
#include <list>
#include <vector>
#include <string>

class HashTable {
    static const int capacity = 7;
    std::vector<std::list<std::pair<std::string, int>>> table;

    int hashFunc(const std::string& key) {
        std::hash<std::string> hasher;
        return hasher(key) % capacity;
    }

public:
    HashTable() : table(capacity) {}

    void put(const std::string& key, int value) {
        int idx = hashFunc(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) {
                kv.second = value;
                return;
            }
        }
        table[idx].push_back({key, value});
    }

    int get(const std::string& key) {
        int idx = hashFunc(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) return kv.second;
        }
        return -1;  // Не найдено
    }

    void remove(const std::string& key) {
        int idx = hashFunc(key);
        table[idx].remove_if([&](const std::pair<std::string, int>& kv) { return kv.first == key; });
    }
};

// Демонстрация
int main() {
    HashTable ht;
    ht.put("cat", 5);
    ht.put("dog", 7);
    std::cout << "Значение для 'cat': " << ht.get("cat") << std::endl; // 5
    ht.remove("cat");
    std::cout << "Значение для 'cat' после удаления: " << ht.get("cat") << std::endl; // -1
}
