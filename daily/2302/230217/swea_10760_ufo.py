import sys

# from pprint import pprint

sys.stdin = open("daily/230217/10760.txt")


T = int(input())
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
for tc in range(1, T + 1):
    arr = []
    ans = 0
    A, B = map(int, input().split())
    for i in range(A):
        lst = list(map(int, input().split()))
        arr.append(lst)
    for i in range(A):
        for j in range(B):
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < A and 0 <= ny < B and arr[i][j] > arr[nx][ny]:
                    cnt += 1
            if cnt > 3:
                ans += 1
    print(f"#{tc} {ans}")
"""
# 영역 탐색
for nr in range(r-1, r+2):
    for nc in range(c-1, c+2):
        if in_range(nr, nc) and land[nr][nc] < land[r][c]:
            now_cnt += 1
"""
