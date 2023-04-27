import sys

# from pprint import pprint
sys.stdin = open("daily/230217/4615.txt")
# 초기 모양 배치
# 인덱스 에러 방지 -> 패딩
# arr[si][sj] = d
# 8방향을 탐색하면서 1 or 2 를 찾음
# 다른 돌은 뒤집는 후보에 추가 이후 같은 돌을 만나면 뒤집기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr 네 방향 0으로 패딩
    arr = [[0] * (N + 2) for _ in range(N + 2)]
    # 초기 위치 설정
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m + 1][m] = arr[m][m + 1] = 1
    # 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 처리
        for di, dj in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ):
            # 해당 방향으로 뻗어나가면서 처리
            t_lst = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if arr[ni][nj] == 0:  # 빈 칸 범위 밖
                    break
                elif arr[ni][nj] != d:  # 다른 돌 만나면 뒤집기
                    t_lst.append((ni, nj))
                else:  # 같은 돌이면 후보들을 뒤집고, 종료
                    while t_lst:
                        ti, tj = t_lst.pop()
                        arr[ti][tj] = d
                    break

    b_cnt = w_cnt = 0
    for lst in arr:
        b_cnt += lst.count(1)
        w_cnt += lst.count(2)
    print(f"#{tc} {b_cnt} {w_cnt}")
