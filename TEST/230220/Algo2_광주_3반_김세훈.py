import sys
# from pprint import pprint
sys.stdin = open('TEST/230220/algo2_sample_in.txt')
T = int(input())
for tc in range(1, 1+T):
    # 배열 범위
    dim = int(input())
    # 전체 지도
    arr = []
    # 방문 여부
    visited = []
    # 내가 지나온 길 기록
    road = []
    x, y = 0, 0
    for i in range(dim):
        lst = list(map(int, input().split()))
        arr.append(lst)
        visited.append([0] * dim)

    while True:
        # 처음 시작점을 지나온 길에 기록
        if len(road) == 0:
            road.append(arr[x][y])
        # 방향이 전환되면 지나온 길에 기록
        elif road[-1] != arr[x][y]:
            road.append(arr[x][y])
        # 인덱스 에러 방지
        if 0 <= x < dim and 0 <= y < dim:
            # 현재 위치를 지나온 길에 기록
            visited[x][y] = 1
            # 0,, 1, 2, 3 방향마다 전진
            if arr[x][y] == 0:
                y += 1
            elif arr[x][y] == 1:
                x += 1
            elif arr[x][y] == 2:
                y -= 1
            else:
                x -= 1
        # 인덱스에 벗어났거나 다음 목적지를 방문한 경우 함수 종료
        if x >= dim or y >= dim or x < 0 or y < 0 or visited[x][y] == 1:
            break
    print(f'#{tc}', end=' ')
    print(*road)
