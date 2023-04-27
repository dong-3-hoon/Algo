from collections import deque
def bfs(sx, sy, ex, ey):
    q = deque([])
    v = [[0]*num for _ in range(num)]
    v[sx][sy] = 1
    q.append((sx, sy))
    while q:
        cx, cy = q.popleft()
        if (cx,cy) == (ex,ey):
            return v[cx][cy]
        for dx, dy in ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)):
            nx,ny = cx+dx,cy+dy
            if 0<=nx<num and 0<=ny<num and v[nx][ny] == 0:
                v[nx][ny] = v[cx][cy] + 1
                q.append((nx,ny))
    return
T = int(input())

for tc in range(1, T+1):
    num = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    ans = bfs(sx,sy,ex,ey)
    print(ans-1)