import sys
from pprint import pprint
sys.stdin = open('color.txt')
T = int(input())

for tc in range(1, T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    color_num = int(input())
    color_info = []
    ans = 0
    for i in range(color_num):
        lst = list(map(int, input().split()))
        color_info.append(lst)
    for j in range(len(color_info)):
        for x in range(color_info[j][0], color_info[j][2]+1):
            for y in range(color_info[j][1], color_info[j][3]+1):
                arr[x][y] += color_info[j][4]
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans += 1
    print(f'#{tc} {ans}')