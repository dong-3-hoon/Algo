"""
# 내 풀이
lst = [55, 7, 78, 12, 42]
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
print(lst)
"""
"""
#sudo code
for i: N-1 ->1 #각 구간의 끝
    for j : 0 -> i-1 #비교 할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1] #큰 원소 오른쪽으로
"""
# 교수님거
arr = list(map(int, input().split()))
N = int(input())
for i in range(N-1, 0, -1):  # 각 구간의 끝
    for j in range(i):  # 비교 할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]  # 큰 원소 오른쪽으로
    print(*arr)
