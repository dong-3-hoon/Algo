import sys

# from pprint import pprint

sys.stdin = open("daily/230228/1288.txt")

T = int(input())

for tc in range(1, T + 1):
    lst = []
    Y = int(input())
    i = 0
    while True:
        i += 1
        X = Y * i
        for j in str(X):
            lst.append(j)
        if len(set(lst)) == 10:
            print(f"#{tc} {Y*i}")
            break
