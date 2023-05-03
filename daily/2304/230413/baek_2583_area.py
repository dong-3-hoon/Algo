from collections import deque
def bfs(i, j):
    global k
    k+= 1
    cnt = 1
    q = deque([])
    q.append((i, j))
    v[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 0 and v[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1
                v[ni][nj] = 1
    return cnt


M, N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

arr = [[0]*N for _ in range(M)]
for i in lst:
    for y in range(i[0], i[2]):
        for x in range(i[1], i[3]):
            arr[x][y] = 1
ans = []
k = 0
v = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and v[i][j] == 0:
            stk = bfs(i,j)
            ans.append(stk)
print(k)
ans.sort()
print(*ans)