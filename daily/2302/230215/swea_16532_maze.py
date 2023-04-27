import sys

# from pprint import pprint

sys.stdin = open("daily/230215/16532.txt")

# 함수 호출
def dfs(x, y, num):
    global ans
    # pprint(arr)
    # 목적지를 만나면 ans를 1로
    if arr[x][y] == 2:
        ans = 1
        return
    arr[x][y] = 1
    # 4개 방향을 탐색한 후 조건에 만족하면 dfs 호출
    if y - 1 >= 0 and arr[x][y - 1] != 1:
        dfs(x, y - 1, num)
    if y + 1 < num and arr[x][y + 1] != 1:
        dfs(x, y + 1, num)
    if x + 1 < num and arr[x + 1][y] != 1:
        dfs(x + 1, y, num)
    if x - 1 >= 0 and arr[x - 1][y] != 1:
        dfs(x - 1, y, num)


T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    arr = []
    ans = 0
    x, y = 0, 0
    for i in range(num):
        lst = list(map(int, input()))
        arr.append(lst)
    for i in range(num):
        for j in range(num):
            if arr[i][j] == 3:
                x, y = i, j
    dfs(x, y, num)
    print(f"#{tc} {ans}")
