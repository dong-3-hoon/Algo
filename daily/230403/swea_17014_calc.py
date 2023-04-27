import sys
sys.stdin = open("daily/230403/17014.txt")
def bfs(N, K):
    q = []
    v[N] = 1
    q.append(N)
    while q:
        t = q.pop(0)
        if t == K:
            return v[t]
        k = t+1
        l = t-1
        m = 2*t
        n = t-10
        if 0<=k<1000001 and (v[k] == 0 or v[k] == -1):
            v[k] = v[t] + 1
            q.append(k)
        if 0<=l<1000001 and (v[l] == 0 or v[l] == -1):
            v[l] = v[t] + 1
            q.append(l)
        if 0<=m<1000001 and (v[m] == 0 or v[m] == -1):
            v[m] = v[t]+1
            q.append(m)
        if 0<=n<1000001 and (v[n] == 0 or v[n] == -1):
            v[n] = v[t]+1
            q.append(n)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    v = [0] * 1000001
    v[K] = -1
    ans = bfs(N, K)
    print(f'#{tc} {ans-1}')