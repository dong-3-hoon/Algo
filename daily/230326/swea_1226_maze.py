import sys
def bfs(sx, sy, ex, ey):
    q = []
    q.append((sx, sy))
    v[sx][sy] == 1
    while q:
        cx, cy =q.pop(0)
        if (cx, cy) == (ex, ey):
            return 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<16 and 0<=ny<16 and v[nx][ny] == 0 and arr[nx][ny] != 1:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1
    return 0

sys.stdin = open("daily/230326/1226.txt")
cnt = 1
while cnt < 11:
    num = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    v = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                sx, sy = i, j
            if arr[i][j] == 3:
                ex, ey = i, j
    ans = bfs(sx, sy, ex, ey)
    print(f'#{cnt} {ans}')
    cnt += 1