# Жадный алгоритм для задачи о максимальном разрезе (MAX CUT) Вариант №9

# Ввод рёбер графа вручную
n = 8  # количество вершин
print("Введите количество рёбер:")
m = int(input())
edges = []
print("Введите рёбра (по два числа через пробел, индексация вершин с 0):")
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Инициализация: помещаем первую вершину в первую группу, остальные во вторую
groupA = set([0])
groupB = set(range(1, n))

# Жадно переносим вершины из одной группы в другую, если это увеличивает количество рёбер в разрезе
improved = True
while improved:
    improved = False
    for v in range(n):
        if v in groupA:
            # Если перенос вершины в другую группу увеличит число рёбер в разрезе — переносим
            cut_before = sum(((v in groupA) != (u in groupA)) for u, w in edges if v==u or v==w)
            groupA.remove(v)
            groupB.add(v)
            cut_after = sum(((v in groupA) != (u in groupA)) for u, w in edges if v==u or v==w)
            if cut_after > cut_before:
                improved = True
            else:
                groupB.remove(v)
                groupA.add(v)
        else:
            cut_before = sum(((v in groupA) != (u in groupA)) for u, w in edges if v==u or v==w)
            groupB.remove(v)
            groupA.add(v)
            cut_after = sum(((v in groupA) != (u in groupA)) for u, w in edges if v==u or v==w)
            if cut_after > cut_before:
                improved = True
            else:
                groupA.remove(v)
                groupB.add(v)

# Подсчёт рёбер в разрезе
cut_edges = 0
for u, v in edges:
    if (u in groupA and v in groupB) or (u in groupB and v in groupA):
        cut_edges += 1

'''
Пример входных данных:
Введите количество рёбер:
10
Введите рёбра (по два числа через пробел, индексация вершин с 0):
0 1
0 2
1 3
1 4
2 5
3 6
4 7
5 6
6 7
0 7

Выходные данные:
Группа 1: [0, 3, 4, 5]
Группа 2: [1, 2, 6, 7]
Количество рёбер в разрезе: 9
'''



