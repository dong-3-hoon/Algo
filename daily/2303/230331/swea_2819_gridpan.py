import sys
sys.stdin = open("daily/230331/2819.txt")
def bfs(i, j):
    pass

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str ,input().split())) for _ in range(4)]
    lst = []
    for i in range(4):
        for j in range(4):
            bfs(i, j)