import sys
sys.stdin = open('TEST/230213/algo1_sample_in.txt')
# sys.stdin = open('1.txt')
# from pprint import pprint
T = int(input())

for tc in range(1, 1+T):
    pallet = []
    dim, color_num = map(int, input().split())
    # 맵 생성
    mapp = [[0 for i in range(dim)] for j in range(dim)]
    # 색을 찍는 갯수만큼 저장
    for i in range(color_num):
        lst = list(map(int, input().split()))
        pallet.append(lst)
    # 색 만큼 반복
    for i in range(color_num):
        # 팔레트의 시작부터 끝까지 색을 칠한다.
        for j in pallet:
            for k in range(j[0]-1, j[0]+j[3]-1):  # 범위 설정 못했음 ㅠㅠ
                for l in range(j[1]-1, j[1]+j[2]-1):
                    mapp[k][l] = 1
    # pprint(mapp)
    cnt = 0
    # 지도를 돌면서 1을 만날 때마다 cnt + 1
    for i in mapp:
        for j in i:
            if j == 1:
                cnt += 1
    print(f'#{tc} {cnt}')
