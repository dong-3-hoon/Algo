
import sys
sys.stdin = open('daily/230208/16348.txt')
from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    lst = []
    N, M = map(int, input().split())
    # 맵 작성
    for i in range(N):
        A = list(input())
        lst.append(A)
    #현재 위치를 탐색
    for x in range(N):
        for y in range(N):
            strr = ''
            #현재 위치 기준 가로를 탐색
            #인덱스에러 방지용
            if x + M <= N:
                #현재 위치에서 주어진 수만큼 탐색 후 회문을 비교
                for i in range(x, x+M):
                    strr += lst[i][y]
                if strr == strr[::-1]:
                    print(f'#{tc} {strr}')
            strr =''
            #가로 탐색 후 세로 탐색
            if y + M <= N:
                for i in range(y, y+M):
                    strr += lst[x][i]
                if strr == strr[::-1]:
                    print(f'#{tc} {strr}')