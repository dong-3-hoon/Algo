import sys
sys.stdin = open('daily/230209/3143.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    str1, str2 = map(list, input().split())
    #리무브는 앞부터 빠진다.
    while True:
        ans = 0
        stk = 0
        #str1의 길이가 더 작으면 stk에 길이만큼 추가한다.
        if len(str1)<len(str2):
            cnt += len(str1)
        #아니면 판별을 시작한다.
        else:
            for stn in range(len(str1)-len(str2)):
                cnt = 0
                for i in range(len(str2)):
                    #현재문자와 판별문자가 같을 때
                    if str1[stn+i] == str2[i]:
                        cnt += 1
                    if cnt == len(str2):
                        stk += 1