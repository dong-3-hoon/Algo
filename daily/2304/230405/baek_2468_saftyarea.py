import sys
sys.stdin = open("daily/230405/2468.txt")
from collections import deque
def bfs(i,j,k):
    global cnt
    cnt += 1
    q = deque([])
    v[i][j] = 1
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<num and 0<=nj<num and arr[ni][nj] > k and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1

num = int(input())
ans = 0
arr = [list(map(int, input().split())) for _ in range(num)]
max_v = max(map(max, arr))
for k in range(max_v+1):
    cnt = 0
    v = [[0] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if arr[i][j] >k and v[i][j] == 0:
                bfs(i,j,k)
    if cnt>ans:
        ans=cnt
print(ans)