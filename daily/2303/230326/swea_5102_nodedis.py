def bfs(start, end):
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        t= q.pop(0)
        for i in G[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)
    start, end = map(int, input().split())
    visited = [0] * (V+1)
    bfs(start, end)
    if visited[end]:
        print(f'#{tc+1} {visited[end]-1}')
    else:
        print(f'#{tc+1} {0}')