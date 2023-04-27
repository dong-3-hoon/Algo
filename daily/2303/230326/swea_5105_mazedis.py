def bfs(xs, ys, xe, ye):
    q=[]
    q.append((xs, ys))
    visited[xs][ys] = 1
    while q:
        cx, cy = q.pop(0)
        if (cx,cy) == (xe, ye):
            return visited[xe][ye] -2
        for dx, dy in ((0, 1), (0,-1), (1, 0), (-1,0)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<num and 0<=ny<num and visited[nx][ny] == 0 and arr[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
    return 0

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input())) for _ in range(num)]
    visited = [[0] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if arr[i][j] == 3:
                xs, ys = i, j
            if arr[i][j] == 2:
                xe, ye = i, j
    ans = bfs(xs, ys, xe, ye)
    print(f'#{tc} {ans}')