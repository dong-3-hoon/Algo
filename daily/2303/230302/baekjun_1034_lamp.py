import sys

from pprint import pprint

sys.stdin = open("daily/230302/1034.txt")

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    lst = [list(map(int, input())) for _ in range(A)]
    K = int(input())
    stk = []
    for i in range(B):
        cnt = 0
        for j in range(A):
            if lst[j][i] == 0:
                cnt += 1
        stk.append(cnt)
    print(stk)
    print(stk.index(max(stk)))
