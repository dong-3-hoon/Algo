import sys

# from pprint import pprint

sys.stdin = open("daily/2302/230228/11315.txt")


T = int(input())
dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]

for tc in range(1, T + 1):
    ans = "NO"
    dim = int(input())
    arr = [list(input()) for _ in range(dim)]
    for x in range(dim):
        for y in range(dim):
            o_num = 0
            if arr[x][y] == "o" and ans == "NO":
                for vec in range(4):
                    o_num = 1
                    for r in range(1, 5):
                        nx = x + dx[vec] * r
                        ny = y + dy[vec] * r
                        if 0 <= nx < dim and 0 <= ny < dim and arr[nx][ny] == "o":
                            o_num += 1
                        else:
                            continue
                        if o_num == 5:
                            ans = "YES"
    print(f"#{tc} {ans}")
