from collections import deque
import sys
sys.stdin = open("daily/230403/17015.txt")
def bfs(s, e):
    q = []
    v = [0]*(V+1)
    q.append(s)
    v[s]=1

    while q:
        c = q.pop(0)
        if c==e:
            return v[e]-1
        for n in adj[c]:
            if v[n]==0:
                q.append(n)
                v[n]=v[c]+1
    return 0

T= int(input())
for test_case in range(1,T+1):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        start, to = lst[2*i], lst[2*i+1]
        adj[start].append(to)
        adj[to].append(start)
    for i in range(V):
        ans = bfs(i, adj)
    print(f'#{test_case} {ans}')