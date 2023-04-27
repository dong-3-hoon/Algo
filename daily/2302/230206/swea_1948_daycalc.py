import sys
sys.stdin = open("day.txt")
T = int(input())

for tc in range(1, T+1):
    bm, bd, am, ad = map(int, input().split())

    month = (am - bm + 1) * 30
    day = ad - am
    print(month, day) 