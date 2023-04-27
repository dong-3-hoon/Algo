def selection_sort_asc(arr, n):
    # 맨 앞자리부터 자리의 주인을 정해준다. 작은숫자부터 차례대로
    for i in range(n - 1):
        min_idx = i
        # i 의 뒤부터 비교를 시작하면서 최솟값을 찾는다.
        for j in range(i + 1, n):
            # 제일 작은 숫자의 인덱스를 찾기
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 반복을 다 돌았으면 제일 작은숫자를 현재 자리 i로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def binary_sort(arr, n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i]<arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

def insert_sort(arr, n):
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

import sys

n = int(sys.stdin.readline())
num_list = [0] * 11

for _ in range(n):  # 카운팅 소트 이용 0~개수만큼 인덱스에 추가
    num_list[int(sys.stdin.readline())] += 1

for i in range(11):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# https://yoonsang-it.tistory.com/49
# https://roytravel.tistory.com/328