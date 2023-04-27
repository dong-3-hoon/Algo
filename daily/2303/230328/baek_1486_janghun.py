import sys
sys.stdin = open("daily/230328/1486.txt")
def comb(idx, r, selected):
    # 종료 조건
    if idx == N:
        if sum(selected) >= B:
            k.append(sum(selected))
        return
    # 재귀 호출
    # 고르고 진행 하던가
    selected.append(lst[idx])
    comb(idx+1, r+1, selected)
    # 고르지 않고 진행 하던가
    selected.pop()
    comb(idx+1, r, selected)

T = int(input())

for tc in range(1, T+1):
    k = []
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    comb(0, 0, [])
    print(f'#{tc} {min(k)-B}')
    