import sys

# from pprint import pprint

sys.stdin = open("daily/230302/1860_.txt")

T = int(input())

for tc in range(1, T + 1):
    # 사람, 만드는 시간, 시간동안 만드는 붕어빵
    ans = "Possible"
    N, M, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    fish_b = 0
    time = 0
    wait = 0
    while time < lst[-1] + 1:
        if time == lst[wait]:
            fish_b -= 1
            wait += 1
        if time != 0 and time % M == 0:
            fish_b += K
        time += 1
        if fish_b < 0:
            ans = "Impossible"
    print(f"#{tc} {ans}")
