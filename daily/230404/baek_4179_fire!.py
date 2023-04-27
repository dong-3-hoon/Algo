import sys
sys.stdin = open("daily/230404/4179.txt")
from collections import deque
def bfs(i, j):
    q = deque([])
    q.append((i, j))
    v[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and v[ni][nj] == 0 and arr[ni][nj] == '.':
                v[ni][nj] = v[ci][cj] + 1
                arr[ni][nj] = 'J'
                q.append((ni, nj))
R, C = map(int, input().split())

arr = [list(map(str, input())) for _ in range(R)]
jihun = []
fire = deque([])
v = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            jihun.append((i,j))
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'F':
            fire.append((i,j))
bfs()
print(v)
print(f_v)