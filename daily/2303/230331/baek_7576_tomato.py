from pprint import pprint
import sys
sys.stdin = open("daily/230331/7576.txt")
from collections import deque
def bfs(i, j, cnt):
    q = []
    v[i][j] = cnt
    arr[i][j] = cnt
    q.append((i, j))
    ci, cj = q.pop(0)
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 0:
            q.append((ni, nj))
            v[ni][nj] = v[ci][cj] + 1
            arr[ni][nj] = arr[ci][cj]+1
T = int(input())
for tc in range(1, T+1):
    M, N = map(int,input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    # 벽 생성
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                v[i][j] = -1
    cnt = 1
    p = 0
    kk = 2*(N+M)
    # 토마토를 탐색
    while True:
        if p == 1:
            break
        for i in range(N):
            for j in range(M):
                if arr[i][j] == cnt and v[i][j] != -1:
                    bfs(i, j, cnt)
            else:
                p = 1
        cnt += 1
    vali = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0:
                vali = 0
            if v[i][j] > cnt:
                cnt = v[i][j]
    if vali == 1:
        print(cnt-1)
    else:
        print(-1)
        