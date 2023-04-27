import sys

from pprint import pprint

sys.stdin = open("daily/230302/1494.txt")


def m():
    min_dis = 9999999999999
    min_i = 0
    min_j = 0
    # 제일 작은 값을 구하는 구문
    for i in range(num):
        for j in range(num):
            if arr[i][j] != 0 and arr[i][j] < min_dis:
                min_dis = arr[i][j]
                min_i, min_j = i, j
    cnt.append(min_dis)
    # 구한 행, 열의 값을 0으로 만드는 구문
    for i in range(num):
        arr[i][min_j] = 0
    for j in range(num):
        arr[min_i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    cnt = []
    ans = 0
    # 지렁이 갯수
    num = int(input())
    # 지렁이의 위치
    lst = [list(map(int, input().split())) for _ in range(num)]
    arr = [[0] * num for _ in range(num)]
    # 각 지렁이가 이동하는 거리 계산
    for i in range(num):
        for j in range(num):
            if j > i:
                arr[i][j] = (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2
    for i in range(num // 2):
        m()
    for i in range(len(cnt)):
        if i % 2 == 0:
            ans += cnt[i]
        else:
            ans -= cnt[i]
    print(ans)
