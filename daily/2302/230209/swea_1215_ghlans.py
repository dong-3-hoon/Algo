
import sys
sys.stdin = open('daily/230209/1215.txt')
from pprint import pprint
tc = 1

while tc<11:
    lst = []
    cnt = 0
    N = 8
    M = int(input())
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
                    cnt += 1
            strr =''
            #가로 탐색 후 세로 탐색
            if y + M <= N:
                for i in range(y, y+M):
                    strr += lst[x][i]
                if strr == strr[::-1]:
                    cnt += 1
    print(f'#{tc} {cnt}')
    tc += 1