import sys
sys.stdin = open('daily/230209/3143.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    typing = 0
    idx = 0
    #문자열 길이가 조정될때는 for문보다 while가 좋다.
    while idx < len(a) - len(b) + 1:
        #패턴 길이 만큼 잘라서 비교
        #같으면 개수 1 증가
        #인덱스를 패턴의 길이만큼 뒤로 이동
        sub = ""
        for i in range(len(b)):
            sub += a[idx + i]
        #잘랐는데 패턴과 일치
        if sub == b:
            typing += 1
            idx += len(b)
        #불일치
        else:
            typing += 1
            idx += 1
    #패턴 길이보다 짧게 남은 글자 처리
    while idx < len(a):
        typing += 1
        idx += 1
    print(f'#{tc} {typing}')