import sys

# from pprint import pprint

sys.stdin = open("daily/230307/1018.txt")

T = int(input())


def valid(n, m, first):
    cnt = 0
    for i in range(n, n + 8):
        for j in range(m, m + 8):
            # 짝수 짝수
            if i % 2 == 0 and j % 2 == 0:
                if arr[i][j] != first:
                    cnt += 1
            # 짝수 홀수
            if i % 2 == 0 and j % 2 != 0:
                if arr[i][j] == first:
                    cnt += 1
            # 홀수 짝수
            if i % 2 != 0 and j % 2 == 0:
                if arr[i][j] == first:
                    cnt += 1
            # 홀수 홀수
            if i % 2 != 0 and j % 2 != 0:
                if arr[i][j] != first:
                    cnt += 1
    return cnt


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    cov_min = 10000
    cnt = 0
    # 8x8 배열을 탐색할 수 있는 범위만 탐색
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            # 흰색, 검은색일때 바꾸는 값 탐색
            first = "W"
            cnt_w = valid(i, j, first)
            first = "B"
            cnt_b = valid(i, j, first)
            if cnt_w < cnt_b:
                cnt = cnt_w
            else:
                cnt = cnt_b
            if cnt < cov_min:
                cov_min = cnt
    print(f"#{tc} {cov_min}")
