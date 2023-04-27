import sys
sys.stdin = open("daily/230328/1244.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    M = int(M)
    v = [0] * 10
    # 교재 최소한의 변경 참조
    for i in N:
        v[int(i)] += 1
    print(v)
    print(v[-M])