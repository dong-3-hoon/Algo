import sys
sys.stdin = open("daily/230330/16979.txt")
T = int(input())
 
 
# row_num : 행 번호 (제품 종류)
# selected : 이전에 고른 공장 중복 체크
# price : 가격의 합
def backtracking(row_num, selected, price):
    global min_v
    # 가지 치기
    # 더이상 가망이 없다면 탐색 종료
    if price >= min_v:
        return
 
    # 종료 조건
    # 제품을 다 골랐다면 ( 행번호가 n )
    if row_num == n:
        min_v = min(min_v, price)
        return
 
    # 재귀 호출
    # 현재 row_num 행에서 고를 열번호 i 를 선택
    for i in range(n):
        # i 열을 고를껀데 , 이 열은 이전에 고른적이 없어야 한다.
        if i not in selected:
            selected.append(i)
            backtracking(row_num + 1, selected, price + factory[row_num][i])
            # 다른 i 를 고르러 가야하니까
            selected.pop()
 
 
for tc in range(1, T + 1):
    n = int(input())
 
    factory = [list(map(int, input().split())) for _ in range(n)]
 
    min_v = 15 * 100
    backtracking(0, [], 0)
 
    print(f"#{tc} {min_v}")