# Пример создания вложенного списка (группы студентов)
teams = [['Alice', 'Bob'], ['Eve', 'Charlie'], ['Dave', 'Frank']]

# Пример создания очереди
from queue import Queue
line = Queue()
line.put(5)
line.put(10)
line.put(15)

# Пример реализации дека
from collections import deque
job_queue = deque()
job_queue.append("job1")
job_queue.append("job2")
job_queue.append("job3")

# Пример приоритетной очереди
from queue import PriorityQueue
priority_tasks = PriorityQueue()
priority_tasks.put((3, "low priority"))
priority_tasks.put((1, "urgent"))
priority_tasks.put((2, "normal"))

# Пример приоритетной очереди с бинарной кучей
import heapq
clients = []
heapq.heappush(clients, (5, "John"))
heapq.heappush(clients, (3, "Anna"))
heapq.heappush(clients, (7, "Zara"))
heapq.heappush(clients, (1, "Mia"))
