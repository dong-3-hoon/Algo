import sys
sys.stdin = open('daily/230209/1979_.txt')
from pprint import pprint
def veli(dim, ans, num):
    for x in range(dim):
        cnt = 0
        for y in range(dim):
            if lst[x][y] == 1:
                cnt += 1
            if lst[x][y] == 0:
                cnt = 0
                #다음 값이 0이거나 배열의 마지막이어야 함
            if cnt == num and (y == dim-1 or lst[x][y+1] == 0):
                ans +=1
    return ans
T = int(input())
for tc in range(1, T+1):
    dim, num = map(int, input().split())
    cnt = 0
    ans = 0
    lst = [list(map(int, input().split())) for i in range(dim)]
    pprint(lst)
    ans = veli(dim, ans, num)
    for i in range(dim):
        for j in range(dim):
            if i>j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    pprint(lst)
    ans = veli(dim, ans, num)
    print(f'#{tc} {ans}')