import sys
sys.stdin = open('daily/230213/16478.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    arr =[]
    for i in range(len(string)):
        if len(arr) == 0:
           arr.append(string[i])
        else:
            if arr[-1] == string[i]:
                arr.pop()
            else:
                arr.append(string[i])
    print(f'#{tc} {len(arr)}')