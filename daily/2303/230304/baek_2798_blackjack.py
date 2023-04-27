import sys

# from pprint import pprint

sys.stdin = open("daily/230304/2798.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    a, b, c = 0, 1, 2
    cnt = []
    while True:
        if a == N-2:
            break
        if M>= (lst[a]+lst[b]+lst[c]):
            cnt.append(lst[a]+lst[b]+lst[c])
        c += 1
        if c == N:
            b += 1
            c= b + 1
        if b == N-1:
            a += 1
            b = a+1
            c = b+1
    print(max(cnt))