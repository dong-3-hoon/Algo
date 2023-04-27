import copy
import sys
sys.stdin = open('ladder.txt')
def dfs(x, y, n_ladder, st):
    #도착점에 도달했을 시 시작 y값을 리턴
    if n_ladder[x][y] == 2:
        return st
    #탐색한 사다리에는 3을 저장해서 다음 탐색시 배제
    n_ladder[x][y] = 3
    #벡터는 우 좌 하를 탐색
    dx = [0, 0, 1]
    dy = [1, -1, 0]
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        # 사다리의 끝에 도달하면 -1을 바로 리턴
        if nx == 100:
            return -1
        #인덱스 에러 제거 및 사다리의 1이나 2를 탐색
        if 0 <= nx < 100 and 0 <= ny < 100 and (n_ladder[nx][ny] == 1 or n_ladder[nx][ny] == 2):
            k = dfs(nx, ny, n_ladder, st)
            #리턴값이 -1이면 사다리를 모두 탐색했으므로 빠르게 종료
            if k == -1:
                return -1
            if k == st:
                return st

while True:
    T = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    #0,0 ~ 0,99까지 진행하며 1을 탐색
    for y in range(100):
        x = 0
        #값이 1이면 사다리 타기 진행
        if ladder[x][y] == 1:
            #현재 y값을 저장
            st = y
            # 딥카피 활용 새로운 사다리를 생성해서 기존 사다리와 겹치는 문제 해결
            n_ladder = copy.deepcopy(ladder)
            st = dfs(x, y, n_ladder, st)
            # 반환값이 -1 이상이면 출력
            if st > -1:
                print(f'#{T} {st}')
    if T == 10:
        break