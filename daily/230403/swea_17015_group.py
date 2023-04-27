from collections import deque
import sys
sys.stdin = open("daily/230403/17015.txt")
def bfs(start):
    global cnt
    cnt += 1
    q = deque([])
    q.append(start)
    v[start] = 1
    while q:
        t = q.popleft()
        for i in G[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t] + 1
T = int(input())

for tc in range(1,T+1):
    cnt = 0
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    v = [0] *(N+1)
    for i in range(M):
        start, to = lst[2*i], lst[2*i+1]
        G[start].append(to)
        G[to].append(start)
    for i in range(1, N+1):
        if v[i] == 0:
            bfs(i)
    print(f'#{tc} {cnt}')
