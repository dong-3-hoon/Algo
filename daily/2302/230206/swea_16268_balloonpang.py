import sys
sys.stdin = open("balloonpang.txt")
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for x in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt_max = 0
    for x in range(N):
        for y in range(M):
            cnt = 0
            cnt += arr[x][y]
            for k in range(4):
                nx, ny = dx[k]+x, dy[k]+y
                if 0<=nx<N and 0<=ny<M: #인덱스 에러 방지
                    cnt += arr[nx][ny]
            if cnt > cnt_max:
                cnt_max = cnt
    print(f'#{tc} {cnt_max}')