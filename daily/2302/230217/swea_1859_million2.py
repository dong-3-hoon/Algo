import sys

# from pprint import pprint
sys.stdin = open("daily/230217/1859.txt")

T = int(input())
# 뒤부터 자신보다 작다면 판매 크다면 자기자신을 갱신
for tc in range(1, 1 + T):
    N = int(input())
    lst = list(map(int, input().split()))
    mx, ans = 0, 0
    # i 부터 끝까지 최대값 찾기
    for n in lst[::-1]:
        if mx > n:
            ans += mx - n
        else:
            mx = n
    print(f"#{tc} {ans}")
