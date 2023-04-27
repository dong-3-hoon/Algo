def Quick_sort(arr):
    # 배열 길이가 1이면 그대로 return
    if len(arr) <= 1:
        return arr
    # pivot의 위치 고려 X, 0번째 인덱스를 pivot으로 항상 고정하고 생각
    # pivot 뺀 나머지를 tail 리스트에 넣는다
    pivot = arr[0]
    tail = arr[1:]
    
    # tail을 하나씩 돌면서 pivot 값보다 작으면 left
    # 크면 right에 넣는다
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    # left, right 재귀 호출.
    return Quick_sort(left) + [pivot] + Quick_sort(right)

import sys
sys.stdin = open("daily/230329/sort.txt")
T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    tmp = [0] * len(A)
    A = Quick_sort(A)
    print(A)