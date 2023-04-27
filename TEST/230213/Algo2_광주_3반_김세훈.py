import sys
sys.stdin = open('TEST/230213/algo2_sample_in.txt')
# sys.stdin = open('1.txt')
from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    arr = []
    # 전체 지도(여기에 두더지, 망치 모두 존재)
    mapp = [[0 for i in range(10)] for j in range(10)]
    # 두더지가 나오는 횟수
    head_num = int(input())
    # 망치의 최초 위치
    ham_x, ham_y = map(int, input().split())
    # 두더지가 나오는 총 정보
    for i in range(head_num):
        xys = list(map(int, input().split()))
        arr.append(xys)
    # 게임 시작
    cnt = 0
    for i in arr:
        # 현재 두더지 위치
        time = i[2]
        while time > 0:
            # 두더지가 해머보다 오른쪽
            if i[1] > ham_y:
                ham_y += 1
            # 두더지가 해머보다 왼쪽
            elif i[1] < ham_y:
                ham_y -= 1
            # 두더지가 해머보다 위
            elif i[0] < ham_x:
                ham_x -= 1
            # 두더지가 해머보다 아래
            elif i[0] > ham_x:
                ham_x += 1
            # 두더지를 잡은 경우 점수를 올리고 시간을 0으로 만들어 반복을 종료
            if ham_x == i[0] and ham_y == i[1]:
                cnt += 1
                time = 0
            time -= 1
    print(f'#{tc} {cnt}')