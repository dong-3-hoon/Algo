import sys
sys.stdin = open('daily/230213/16467.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    lst = input()
    cnt = []
    answer = 1
    for i in lst:
        if i == '{' or i == '(' or i == '[':
            cnt.append(i)
        if i =='}' or i == ')' or i == ']':
            if len(cnt) == 0:
                answer = 0
                break
            b = cnt.pop()
            if not ((b == "(" and i == ")") or (b=="{" and i =='}') or (b == "[" and i ==']')):
                answer = 0
                break
    if len(cnt) > 0:
        answer = 0
    print(f'#{tc} {answer}')