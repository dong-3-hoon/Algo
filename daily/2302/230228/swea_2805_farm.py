import sys

# from pprint import pprint

sys.stdin = open("daily/230228/2805.txt")

T = int(input())

for tc in range(1, T + 1):
    dim = int(input())
    cnt = 0
    ans = 0
    lst = [list(map(int, input())) for _ in range(dim)]
    mid = dim // 2
    start, end = mid, mid + 1
    # 처음 반복은 1부터 dim 까지 시작은 -1, 끝은 +1 씩 더해서 범위를 늘림 
    while cnt < dim // 2:
        for i in range(start, end):
            ans += lst[cnt][i]
        cnt += 1
        start -= 1
        end += 1
    # 두번째 반복은 최대부터 1까지 범위를 줄임
    while cnt < dim:
        for i in range(start, end):
            ans += lst[cnt][i]
        cnt += 1
        start += 1
        end -= 1
    print(f"#{tc} {ans}")
