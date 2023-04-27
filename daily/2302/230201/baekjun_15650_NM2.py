
def backtrack(start):
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return 

    for i in range(start, N+1):
        if i not in lst:
            lst.append(i)
            backtrack(i+1)
            lst.pop()
N,M = list(map(int, input().split()))
lst = []
backtrack(1)

