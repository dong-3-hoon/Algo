import sys

# from pprint import pprint
sys.stdin = open("TEST/230227/algo1_sample_in.txt")

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    arr = []  # 나무 정보 배열
    stk1, stk2 = [], []  # 나무의 가격정보 배열
    cnt1, cnt2 = 0, 0  # 나무의 갯수
    ex_tree1, ex_tree2 = 0, 0  # 가장 비싼 나무
    row1, row2 = 0, 0  # 비싼 나무의 줄 정보
    # 나무 arr 생성
    for i in range(a):
        lst = list(map(int, input().split()))
        arr.append(lst)

    for x in range(a):
        for y in range(b):
            # 짝수 열의 나무 정보
            if y % 2 == 0:
                cnt1 += 1
                stk1.append(arr[x][y])
                # 현재 나무 가격이 최대값보다 크다면 비싼 나무 가격, 나무의 줄 정보 갱신
                if arr[x][y] >= ex_tree1:
                    ex_tree1 = arr[x][y]
                    if row1 < y+1:
                        row1 = y + 1
            # 홀수 열의 나무 정보
            else:
                cnt2 += 1
                stk2.append(arr[x][y])
                # 현재 나무 가격이 최대값보다 크다면 비싼 나무 가격, 나무의 줄 정보 갱신
                if arr[x][y] >= ex_tree2:
                    ex_tree2 = arr[x][y]
                    if row2 < y+1:
                        row2 = y + 1
    # 나무 가격의 총 합이 더 큰 쪽의 정보를 출력
    if sum(stk1) > sum(stk2):
        print(f"#{tc} {sum(stk1)} {cnt1} {ex_tree1} {row1}")
    else:
        print(f"#{tc} {sum(stk2)} {cnt2} {ex_tree2} {row2}")
