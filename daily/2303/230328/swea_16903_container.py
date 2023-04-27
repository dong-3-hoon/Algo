import sys
sys.stdin = open("daily/230328/16903.txt")

# 조합해서 맞는 무게가 있다면 넣기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    con_w = list(map(int, input().split()))
    tru_w = list(map(int, input().split()))
    carry = []
    con_w.sort()
    tru_w.sort()
    for i in tru_w:
        for j in range(i):
            if i-j in con_w:
                carry.append(i-j)
                con_w.remove(i-j)
                break
    print(f'#{tc} {sum(carry)}')