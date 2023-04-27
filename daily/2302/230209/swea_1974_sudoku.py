import sys
sys.stdin = open('daily/230209/1974.txt')
from pprint import pprint
#사각형 검증 코드
def sq_veli(x, y, sset, cnt, lst):
    #각 숫자를 집합에 집어넣음
    for i in range(x, x+3):#1,1번
        for j in range(y, y+3):
            sset.add(lst[i][j])
    #집합의 길이가 9 미만이면 스도쿠 실패
    if len(sset) < 9:
        cnt=0
    sset=set([])
    return cnt

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt=1
    lst=[] #생성 스도쿠 배열
    for i in range(9):# 맵 생성
        lst.append(list(map(int, input().split())))
    sset=set([])
    for j in range(9): #x축 스도쿠 검증
        for k in lst[j]:
            sset.add(k)
        if len(sset) < 9:
            cnt=0
        sset=set([])
    for a in range(9): #y축 스도쿠 검증
        for b in range(9):
            sset.add(lst[b][a])
        if len(sset) < 9:
            cnt=0
        sset=set([])
    #사각형 검증
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            cnt = sq_veli(i, j, sset, cnt, lst)
    #pprint(lst)
    print(f"#{test_case} {cnt}")
    
