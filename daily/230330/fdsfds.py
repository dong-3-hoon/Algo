def bfs(i, j):
    q = []
    v[i][j] = 1
    q.append((i, j))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] != -1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
M, N = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            v[i][j] = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i, j)
