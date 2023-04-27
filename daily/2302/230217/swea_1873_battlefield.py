import sys

# from pprint import pprint

sys.stdin = open("daily/230217/1873.txt")
T = int(input())

for tc in range(1, T + 1):
    arr = []
    x, y = map(int, input().split())
    for i in range(x):
        lst = list(input())
        arr.append(lst)
    for i in range(y):
        for j in range(x):
            if (
                arr[j][i] == ">"
                or arr[j][i] == "<"
                or arr[j][i] == "^"
                or arr[j][i] == "v"
            ):
                now_x, now_y = j, i
    turn_num = int(input())
    turn = input()
    for i in range(len(turn)):
        # 위로 한 칸 이동
        if turn[i] == "U":
            arr[now_x][now_y] = "^"
            if 0 <= now_x - 1 < x:
                if arr[now_x - 1][now_y] == ".":
                    arr[now_x - 1][now_y] = "^"
                    arr[now_x][now_y] = "."
                    now_x = now_x - 1
        # 아래로 이동
        elif turn[i] == "D":
            arr[now_x][now_y] = "v"
            if 0 <= now_x + 1 < x:
                if arr[now_x + 1][now_y] == ".":
                    arr[now_x + 1][now_y] = "v"
                    arr[now_x][now_y] = "."
                    now_x = now_x + 1
        # 왼쪽으로 이동
        elif turn[i] == "L":
            arr[now_x][now_y] = "<"
            if 0 <= now_y - 1 < y:
                if arr[now_x][now_y - 1] == ".":
                    arr[now_x][now_y - 1] = "<"
                    arr[now_x][now_y] = "."
                    now_y = now_y - 1
        # 오른쪽으로 이동
        elif turn[i] == "R":
            arr[now_x][now_y] = ">"
            if 0 <= now_y + 1 < y:
                if arr[now_x][now_y + 1] == ".":
                    arr[now_x][now_y + 1] = ">"
                    arr[now_x][now_y] = "."
                    now_y = now_y + 1
        else:
            # 위로 포탄 발사
            if arr[now_x][now_y] == "^":
                for j in range(now_x, -1, -1):
                    if arr[j][now_y] == "#":
                        break
                    if arr[j][now_y] == "*":
                        arr[j][now_y] = "."
                        break
            # 아래로 포탄 발사
            elif arr[now_x][now_y] == "v":
                for j in range(now_x, x, 1):
                    if arr[j][now_y] == "#":
                        break
                    if arr[j][now_y] == "*":
                        arr[j][now_y] = "."
                        break
            # 왼쪽으로 포탄 발사
            elif arr[now_x][now_y] == "<":
                for j in range(now_y, -1, -1):
                    if arr[now_x][j] == "#":
                        break
                    if arr[now_x][j] == "*":
                        arr[now_x][j] = "."
                        break
            # 오른쪽으로 포탄 발사
            elif arr[now_x][now_y] == ">":
                for j in range(now_y, y, 1):
                    if arr[now_x][j] == "#":
                        break
                    if arr[now_x][j] == "*":
                        arr[now_x][j] = "."
                        break
    print(f"#{tc}", end=" ")
    for i in range(x):
        for j in range(y):
            print(arr[i][j], end="")
        print()
