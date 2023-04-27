import sys
sys.stdin = open('daily/230210/1216.txt')
from pprint import pprint

tc = 1

while tc < 11:
    lst = []
    cnt = 0
    N = 100
    M = int(input())
    # 맵 작성
    for i in range(N):
        A = list(input())
        lst.append(A)
    strr_max = 0
    # 현재 위치를 지정
    for x in range(N):
        for y in range(N):
            # 끝나는 위치는 100->0까지 점점 감소
            for K in range(100, 0, -1):
                strr = ''
                # 맥스값보다 조사 범위가 큰 값의 문자열만을 탐색
                if K - x > strr_max:
                    for i in range(x, K):
                        strr += lst[i][y]
                    if strr == strr[::-1] and len(strr)>strr_max:
                        strr_max = len(strr)
                strr = ''
                if K - y > strr_max:
                    for i in range(y, K):
                        strr += lst[x][i]
                    if strr == strr[::-1] and len(strr)>strr_max:
                        strr_max = len(strr)
    print(f'#{tc} {strr_max}')
    tc += 1