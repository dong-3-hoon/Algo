import sys

# from pprint import pprint
sys.stdin = open("daily/230220/16638.txt")

T = int(input())

for tc in range(1, T + 1):
    length, rot_n = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f"#{tc} {lst[rot_n % length]}")
