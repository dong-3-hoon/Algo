import sys

# from pprint import pprint
sys.stdin = open("daily/230217/1859.txt")

T = int(input())
# 최댓값을 찾아서 최대값 이전의 것들은 모두 산 후 최대값에 판다
# 이후 최대값을 다시 찾아서 사이의 것들을 모두 산 후 새로운 최대값에 판다
for tc in range(1, 1 + T):
    N = int(input())
    lst = list(map(int, input().split()))
    i, ans = 0, 0
    while i < N:
        # i 부터 끝까지 최대값 찾기
        i_mx = i
        for j in range(i + 1, N):
            if lst[i_mx] < lst[j]:
                i_mx = j
        # i ~ i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]
        i = i_mx + 1
    print(f"#{tc} {ans}")
