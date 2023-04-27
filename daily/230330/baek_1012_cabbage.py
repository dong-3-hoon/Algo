from pprint import pprint
def bfs(i, j, cnt):
    q = []
    v[i][j] = 1
    q.append((i, j))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = 1

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)
    print(cnt)