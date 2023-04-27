import sys

sys.stdin = open("wlqgkq.txt")
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    cnt = 0
    for i in range(1<<12):
        kk = []
        for j in range(len(lst)):
            if i & (1<<j):# i의 j번 비트가 1인 경우
                #print(lst[j], end=", ") # j번 원소 출력
                kk.append(lst[j])
        if len(kk) == N and sum(kk) == K:
            cnt +=1
    print(f'#{tc} {cnt}')