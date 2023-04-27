import sys

# from pprint import pprint
sys.stdin = open("daily/230225/5688.txt")

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    ans = -1
    for i in range(int(num**(1/3))-1, int(num**(1/3))+2):
        if i**3 == num:
            ans = i
    print(f'#{tc} {ans}')