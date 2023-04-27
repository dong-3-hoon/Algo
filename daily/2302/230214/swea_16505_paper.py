import sys

sys.stdin = open("daily/230214/16505.txt")
# from pprint import pprint

"""
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = 2
    if (N // 10) % 2 == 0: # 20, 40, 60 ...
        for i in range((N//10)//2+1):
            ans = 4**i +ans
        print(f'#{tc} {ans+1}')
    else: # 10, 30, 50 ...
        # 이후에는 이전의 값 *4 + 이전의 값
        for i in range((N//10)//2+1):
            ans = 4**i +ans
        print(f'#{tc} {ans-1}')
"""


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return paper(n - 1) + paper(n - 2) * 2


def paper_dp(n):
    dp = [0] * 10001
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    return dp[n]


T = int(input())

for tc in range(1, T + 1):
    n = int(input()) // 10  # n = 1, 2, 3, 4..

    print(f"#{tc} {paper_dp(n)}")
