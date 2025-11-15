// Двусвязный список элемент структуры
struct Element {
    int value;
    Element *prev;
    Element *next;
};

// Очередь строк
std::queue<std::string> namesQueue;
namesQueue.push("Alice");
namesQueue.push("Bob");
namesQueue.push("Eve");

// Дек
std::deque<int> numbers = {10, 20, 30};

// Приоритетная очередь для int
std::priority_queue<int> intPQ;
intPQ.push(100);
intPQ.push(50);
intPQ.push(75);

// Приоритетная очередь для пользовательских структур
struct Job {
    std::string name;
    int priority;
};

struct CompareJobs {
    bool operator()(Job const& a, Job const& b) {
        return a.priority > b.priority; // Минимальная очередь по приоритету
    }
};

std::priority_queue<Job, std::vector<Job>, CompareJobs> jobPQ;
jobPQ.push({"Cleaning", 3});
jobPQ.push({"Installing", 1});
jobPQ.push({"Repair", 2});
