import sys
sys.stdin = open("daily/230330/1865.txt")
T = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = [list(map(int, input().split())) for _ in range(num)]