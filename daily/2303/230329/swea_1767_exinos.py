import sys
sys.stdin = open("daily/230329/1767.txt")
T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for tc in range(1, T+1):
    num = int(input())
    lst = []
    arr = [list(map(int, input().split())) for _ in range(num)]

    for i in range(num):
        for j in range(num):
            if arr[i][j] == 1:
                lst.append([i, j])
    road = [0] * len(lst)
    for i in lst:
        if i[0] == 0 or i[0] == num-1 or i[1] == 0 or i[1] == num-1:
            continue
        else:
            # 탐색 - 끝까지 쭉 간 후 연결할 수 있는 공간이면 road[i] += 1
            pass