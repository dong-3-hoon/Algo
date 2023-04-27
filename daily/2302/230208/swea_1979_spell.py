import sys
sys.stdin = open('daily/230208/1979_.txt')
from pprint import pprint

T = int(input())
dx = [0, 1]
dy = [1, 0]
for tc in range(1, T+1):
    dim, num = map(int, input().split())

    lst = [list(map(int, input().split())) for i in range(dim)]
    pprint(lst)
    #현재 위치가 1이면 갈 수 있는 만큼 벡터를 이동시켜서 num과 같다면 
    #이 전 위치가 1이면 안됨.
    for x in range(dim):
        for y in range(dim):
            cnt = 0
            vec = 0
            if lst[x][y] == 1:
                #내가 나아갈 수 있을만큼 최대한 나아가야 함
                while True:
                    nx, ny = dx[vec]+x, dy[vec]+y
                    #벽을 부딪치거나 0이라면 cnt를 저장하고 다음 위치를 탐색
                    if 0 <= nx < dim and 0 <= ny < dim and lst[nx][ny] == 0:
                                x, y = nx, ny
                    else:
                        # 방향을 바꾸고 다음 위치 계산후 현재 위치를 다음 위치로 변경
                        vec += 1
                        if vec == 2:
                            vec = 0
                        x = x + dx[vec]
                        y = y + dy[vec]