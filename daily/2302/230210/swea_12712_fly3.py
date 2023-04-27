import sys
sys.stdin = open('daily/230210/12712.txt')
from pprint import pprint
#십자, X자
dx = [[1, -1, 0, 0], [1, 1, -1, -1]]
dy = [[0, 0, 1, -1], [1, -1, 1, -1]]
T = int(input())

for tc in range(1, T+1):
    maap = []
    dim, ran = map(int, input().split())
    for i in range(dim):
        lst = list(map(int, input().split()))
        maap.append(lst)
    cnt_max = 0
    rep = 0
    #위치
    for x in range(dim):
        for y in range(dim):
            #벡터 조정
            for k in range(2):
                cnt = 0
                cnt += maap[x][y]
                for l in range(4):
                    #분사 범위
                    #여기서 한 번 더 진행해야 하는데
                    for q in range(1, ran):
                        nx, ny = q*dx[k][l]+x, q*dy[k][l]+y
                        if 0<=nx<dim and 0<=ny<dim: #인덱스 에러 방지
                            cnt += maap[nx][ny]
                if cnt > cnt_max:
                    cnt_max = cnt
                cnt = 0
    print(f'#{tc} {cnt_max}')