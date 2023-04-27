import sys
sys.stdin = open("daily/230405/1194.txt")
def bfs():
    pass

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    