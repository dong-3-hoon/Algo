import sys
sys.stdin = open("daily/230404/17029.txt")
T = int(input())

for tc in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]
