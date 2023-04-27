def backtrack():
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            backtrack()
            lst.pop()
        # 1 1 1 1, 1 1 1 2, 1 1 1 3, 1 1 1 4, 1 1 2 1, 
        # 1 1 2 2, 1 1 2 3, 1 1 2 4, 1 1 3 1, 1 1 3 2, 1 1 3 3, ...
N, M = map(int, input().split())
lst = []
backtrack()