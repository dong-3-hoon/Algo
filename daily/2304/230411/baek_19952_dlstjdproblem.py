from collections import deque
def bfs(sx, sy, ex, ey, F):
    q = deque([])
    q.append((sx-1, sy-1, F))
    v = [[0] * W for _ in range(H)]
    v[sx-1][sy-1] = 1
    while q:
        cx, cy, F = q.popleft()
        # 도착
        if v[ex-1][ey-1] != 0:
            return v[ex-1][ey-1]
        # 남은 힘이 0일 때 반복을 진행(힘이 남은 경우의 수 탐색)
        if F==0:
            continue
        for dx, dy in ((0,1), (0,-1), (1, 0), (-1,0)):
            nx, ny = cx+dx, cy+dy
            # 갈 수 있는 곳을 append
            if 0<=nx<H and 0<=ny<W and v[nx][ny] == 0 and (arr[nx][ny]-arr[cx][cy])<=F:
                q.append((nx, ny, F-1))
                v[nx][ny] = v[cx][cy] + 1
    return -1


T = int(input())
for tc in range(1, T+1):
    # 높이, 넓이, 장애물 갯수, 힘, 시작, 끝
    H, W, O, F, sx, sy, ex, ey = map(int, input().split())
    lst = []
    for i in range(O):
        a, b, c = map(int, input().split())
        lst.append((a,b,c))
    arr = [[0] * W for _ in range(H)]
    for i in range(O):
            # 맵에 장애물 위치에 장애물 높이만큼 설치
            arr[lst[i][0]-1][lst[i][1]-1] = lst[i][2]
    ans = bfs(sx, sy, ex, ey, F)
    if ans == -1:
        print("인성 문제있어??")
    else:
        print("잘했어!!")