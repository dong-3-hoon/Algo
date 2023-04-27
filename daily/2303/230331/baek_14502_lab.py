from pprint import pprint
def bfs(i, j, now):
    global h
    h+= 1
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<num and 0<=nj<num and arr[ni][nj] == now and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))

def bfs2(i, j, now):
    global n
    n+= 1
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<num and 0<=nj<num and arr[ni][nj] == now and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))

num = int(input())

arr = [list(map(str, input())) for _ in range(num)]
h = 0
n = 0
# 킹반인
v = [[0] * num for _ in range(num)]
for i in range(num):
    for j in range(num):
        if arr[i][j] == 'R' and v[i][j] == 0:
            now = 'R'
            bfs(i, j, now)
        if arr[i][j] == 'B' and v[i][j] == 0:
            now = 'B'
            bfs(i, j, now)
        if arr[i][j] == 'G' and v[i][j] == 0:
            now = 'G'
            bfs(i, j, now)
# 색약
for i in range(num):
    for j in range(num):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
v = [[0] * num for _ in range(num)]
for i in range(num):
    for j in range(num):
        if arr[i][j] == 'R' and v[i][j] == 0:
            now = 'R'
            bfs2(i, j, now)
        if arr[i][j] == 'B' and v[i][j] == 0:
            now = 'B'
            bfs2(i, j, now)
print(h, n)