T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    # 2차원 배열에 접근
    arr = [[0] * N for _ in range(N)]
    lst = [i for i in range(1, (N*N) + 1)]
    # 현재위치 설정
    r, c = 0, 0
    d = 0
    for i in range(1, N*N + 1): # i 는 달팽이 안에 들어갈 숫자, 1부터 증가
        #현재 위치에서 1만큼 넣기
        arr[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            # 방향을 바꾸고 다음 위치 계산후 현재 위치를 다음 위치로 변경
            d += 1
            if d == 4:
                d = 0
            r = r + dr[d]
            c = c + dc[d]

    print(f"#{tc}")
    for q in range(len(arr)):
        print(*arr[q])