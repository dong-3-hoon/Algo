T = int(input())
def bfs(s, e):
    q = []
    v = [0] * (N+1)
    v[s] = 1
    q.append(s)
    while q:
        t = q.pop(0)
        if t == e:
            return v[e]-1
        for n in kk[t]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[t]+1
    return 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    kk = [[] for _ in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        kk[s].append(e)
        kk[e].append(s)
    s, e = map(int, input().split())
    ans = bfs(s, e)
    print(ans)