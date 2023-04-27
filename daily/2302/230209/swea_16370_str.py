import sys
sys.stdin = open('daily/230209/16370.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for j in range(len(str1)):
        cnt = 0
        for i in range(len(str2)):
            if str1[j] == str2[i]:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(f'#{tc} {ans}')