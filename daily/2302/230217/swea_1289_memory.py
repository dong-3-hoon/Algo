import sys

# from pprint import pprint

sys.stdin = open("daily/230217/1289.txt")

T = int(input())

for tc in range(1, T + 1):
    ori = list(map(int, input()))
    now = []
    for i in range(len(ori)):
        now.append(0)
    cnt = 0
    for i in range(len(ori)):
        if ori[i] != now[i]:
            if ori[i] == 0:
                cnt += 1
                for j in range(i, len(ori)):
                    now[j] = 0
            elif ori[i] == 1:
                cnt += 1
                for j in range(i, len(ori)):
                    now[j] = 1
    print(f"#{tc} {cnt}")
