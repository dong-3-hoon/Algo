from collections import deque
def bfs(i, j):
    global ar_max
    q = deque([])
    q.append((i, j))
    v = [[0] * num for _ in range(num)]
    v[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<num and 0<=nj<num and v[ni][nj] == 0 and arr[ni][nj]>arr[ci][cj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
    k = max(map(max, v))
    if k > ar_max:
        ar_max = k
num = int(input())
ar_max = 0
arr = [list(map(int, input().split())) for _ in range(num)]
for i in range(num):
    for j in range(num):
        bfs(i, j)
print(ar_max)