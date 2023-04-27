import sys
sys.stdin = open('daily/230210/5356.txt')
from pprint import pprint

T = int(input())

for tc in range(1, 1+T):
    string = []
    string_max = 0
    #맵 생성, 문자열 최대 길이 저장
    for i in range(5):
        lst = list(input())
        if len(lst)>string_max:
            string_max = len(lst)
        string.append(lst)
    #문자열이 부족한 것들을 추가해서 dim을 맞춘다.
    for i in range(5):
        if len(string[i]) != string_max:
            for j in range(string_max - len(string[i])):
                string[i].append("")
    print(f'#{tc}', end=' ')
    for y in range(string_max):
        for x in range(5):
            print(f'{string[x][y]}', end="")
    print()