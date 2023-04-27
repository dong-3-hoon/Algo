from collections import deque
# 문명의 1년을 증가시킴
def bfs(year):
    q=deque([])
    v=[[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if arr[x][y] == year and v[x][y] == 0:
                v[x][y]=1
                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<N and 0<=ny<N and v[nx][ny]==0 and arr[nx][ny]==0:
                        v[nx][ny] = 1
                        arr[nx][ny] = year+1
# 모든 문명이 연결됐는지 확인
def veli_bfs(year):
    cnt = 0
    q =deque([])
    v=[[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0 and v[x][y] == 0:
                cnt += 1
                if cnt>1:
                    return 0
                q.append((x,y))
                v[x][y] = 1
                while q:
                    cx, cy = q.popleft()
                    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                        nx, ny = cx+dx, cy+dy
                        if 0<=nx<N and 0<=ny<N and v[nx][ny]==0 and arr[nx][ny] != 0:
                            v[nx][ny] = 1
                            q.append((nx,ny))
    return cnt
N, K = map(int, input().split())# N: arr, K:line
arr = [[0]*N for _ in range(N)]
year, ans = 1, 0
for i in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
while True:
    ans = veli_bfs(year)
    if ans == 1:
        break
    bfs(year)
    year += 1
print(year-1)