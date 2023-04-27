import sys
# from pprint import pprint
sys.stdin = open('TEST/230220/algo1_sample_in.txt')
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
T = int(input())
for tc in range(1, T+1):
    # 배열의 범위
    dim = int(input())
    # 전체 배열
    arr = []
    # 봉우리
    hill = []
    ans = 0
    # 맵 생성
    for i in range(dim):
        lst = list(map(int, input().split()))
        arr.append(lst)
    # 맵 탐색
    for x in range(dim):
        for y in range(dim):
            cnt = 0
            # 인덱스 에러 방지
            if 0 < x < dim-1 and 0 < y < dim-1:
                # 8방향을 탐색
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 자기 자신보다 낮은 봉우리 탐색
                    if arr[nx][ny] < arr[x][y]:
                        cnt += 1
                # 근처 지역 모두 자기 자신보다 낮다면 hill 에 추가
                if cnt == 8:
                    hill.append(arr[x][y])
    # hill 이 0, 1개면 -1
    if len(hill) < 2:
        ans = -1
    # hill 의 개수가 2개 이상이라면 차이를 출력
    else:
        ans = max(hill) - min(hill)
    print(f'#{tc} {ans}')
