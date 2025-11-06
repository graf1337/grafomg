def get_combinations(n, k):
    res = []
    def backtrack(start, combo):
        if len(combo) == k:
            res.append(combo.copy())
            return
        for i in range(start, n + 1):
            combo.append(i)
            backtrack(i + 1, combo)
            combo.pop()
    backtrack(1, [])
    return res

# Пример: n=3, k=2
print(get_combinations(3, 2))
