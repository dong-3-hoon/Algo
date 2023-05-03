from collections import deque
def bfs(a, b):
    q = deque([])
    v=[0] *(n+1)
    q.append(a)
    while q:
        t = q.popleft()
        if t == b:
            return v[t]
        for i in G[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t] + 1

    return -1
n = int(input())
a, b = map(int, input().split())
m = int(input())
G = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
ans = bfs(a, b)
print(ans)