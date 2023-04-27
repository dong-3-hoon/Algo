def bfs(i, j, cnt):
    q = []
    q.append((i, j))
    v[i][j] = cnt
    ci, cj = q.pop(0)
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<M and 0<=nj<N and v[i][j] == cnt and arr[ni][nj] ==0:
            q.append((ni, nj))
            v[ni][nj] = v[i][j] + 1
            arr[ni][nj] = arr[i][j] + 1


import sys
sys.stdin = open("daily/230331/7576.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    v = [[0] * N for _ in range(M)]
    cnt = 1
    while cnt < 2*(N+M):
        for i in range(M):
            for j in range(N):
                if arr[i][j] == 0 and v[i][j] == 0:
                    bfs(i, j, cnt)
        cnt += 1
    print(arr)