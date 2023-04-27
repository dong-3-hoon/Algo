import sys

# from pprint import pprint
sys.stdin = open("daily/230215/1217.txt")


def mul(A, B):
    global ans
    if B == 0:
        return
    else:
        ans *= A
        mul(A, B - 1)


while True:
    ans = 1
    tc = int(input())
    A, B = map(int, input().split())
    mul(A, B)
    print(f'#{tc} {ans}')
    if tc == 10:
        break
