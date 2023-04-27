def bfs(i, j):
    global ans 
    ans += 1
    q=[]
    v[i][j] = 1
    q.append((i, j))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, -1), (1, 0), (-1, 0), (0, 1), (1, 1), (-1,-1), (1, -1), (-1, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ans = 0
    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i, j)
    print(ans)