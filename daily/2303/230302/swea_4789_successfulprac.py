import sys

# from pprint import pprint

sys.stdin = open("daily/230302/4789.txt")

T = int(input())

for tc in range(1, T + 1):
    clap = 0
    hire = 0
    t_hire = 0
    lst = list(map(int, input()))
    for i in range(len(lst)):
        if clap < i:
            hire = i - clap
            clap += hire
            t_hire += hire
        clap += lst[i]
    print(f"#{tc} {t_hire}")
