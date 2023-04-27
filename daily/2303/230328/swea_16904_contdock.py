import sys
sys.stdin = open("daily/230328/16904.txt")
T = int(input())
# 끝나는 시간이 빠른 순으로 정렬을 하는게 해답이다!
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 정렬
    for i in range(N):
        for j in range(N):
            if lst[i][1] < lst[j][1]:
                lst[i], lst[j] = lst[j], lst[i]
    cnt = 1
    end = lst[0][1]
    for i in lst:
        if end<=i[0]:
            end = i[1]
            cnt += 1
    print(f'#{tc} {cnt}')