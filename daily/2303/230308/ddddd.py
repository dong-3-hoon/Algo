import sys

# from pprint import pprint

sys.stdin = open("KSH_SSAFY/daily/230308/ddddd.txt")

T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]
    print(arr)
