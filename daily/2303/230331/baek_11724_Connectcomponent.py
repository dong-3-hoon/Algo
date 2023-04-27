def bfs(s):
    global ans
    ans += 1
    q = []
    q.append(s)
    v[s] = 1
    while q:
        t=q.pop(0)
        for i in G[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t]+1
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
ans = 0
G = [[] for _ in range(N+1)]
for i in lst:
    s, e = i[0], i[1]
    G[s].append(e)
    G[e].append(s)
v = [0] * (N+1)
for i in range(1, N+1):
    if v[i] == 0:
        bfs(i)
print(ans)