lst = [1,2,3,4,5]
N = 5
R = 3

# N개 중에 R개를 고르는 경우의 수

# 1. idx 번째 숫자를 고를지 고르지 않을지 결정
def comb(idx, r, selected):
    # 종료 조건
    if idx == N:
        print(selected)
        # return
    # R개 골랐을때만 출력
    if r == R:
        print(selected)
        return 
    # 재귀 호출
    # 고르고 진행 하던가
    selected.append(lst[idx])
    comb(idx+1, r+1, selected)
    # 고르지 않고 진행 하던가
    selected.pop()
    comb(idx+1, r, selected)
comb(0, 0, [])