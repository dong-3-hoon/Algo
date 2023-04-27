import sys

# from pprint import pprint

sys.stdin = open("daily/230302/5789.txt")

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(Q)]
    arr = [0] * N
    for i in range(Q):
        for j in range(lst[i][0] - 1, lst[i][1]):
            arr[j] = i + 1
    print(f"#{tc}", *arr)
