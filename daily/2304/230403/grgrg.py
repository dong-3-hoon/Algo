import sys
sys.stdin = open("daily/230403/17014.txt")
from collections import deque
def bfs(N, K):
    q = deque([])
    v[N] = 1
    q.append(N)
    while q:
        t = q.popleft()
        if t == K:
            return v[t]
        k = t+1
        l = t-1
        m = 2*t
        n = t-10
        for i in [k, l, m, n]:
            if 0<=i<1000001 and (v[i] == 0 or v[i] == -1):
                v[i] = v[t] + 1
                q.append(i)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    v = [0] * 1000001
    v[K] = -1
    ans = bfs(N, K)
    print(f'#{tc} {ans-1}')