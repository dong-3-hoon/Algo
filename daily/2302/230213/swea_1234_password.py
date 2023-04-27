import sys
sys.stdin = open('daily/230213/1234.txt')
from pprint import pprint

tc = 1
while tc<11:
    leng, num = map(str, input().split())
    arr =[]
    #문자열 길이만큼 반복
    for i in range(int(leng)):
        #정답 문자열에 아무것도 없을시에 추가
        if len(arr) == 0:
            arr.append(num[i])
        else:
            #이전 문자와 현재 문자가 같다면 이전 문자를 pop
            if arr[-1] == num[i]:
                arr.pop()
            else:
                #다르다면 현재 문자를 stack
                arr.append(num[i])
    print(f'#{tc} {"".join(arr)}')
    tc += 1