import sys

# from pprint import pprint

sys.stdin = open("daily/230225/1861_.txt")

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for tc in range(1, T+1):
    x, y = 0, 0
    dim = int(input())
    arr = []
    for i in range(dim):
        lst = list(map(int, input().split()))
        # 아웃풋은 어떤 위치에서 시작해서 몇번 이동이 가능한지
        arr.append(lst)
    # 좌표를