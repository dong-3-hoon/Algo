from collections import deque

# 정점개수, 시작
def dfs(V, N):
    visited[V] = True
    print(V, end=" ")

    for i in G[V]:
        if not visited[i]:
            dfs(i, N)


def bfs(V, N):
    visited = [0] *(N+1)
    q=[]
    q.append(V)
    visited[V] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[i] + 1

# n=정점, m간선, v시작, g맵
N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)
for i in G:
    i.sort()
visited = [0] *(N+1)
dfs(V, N)
print()
bfs(V, N)
print()