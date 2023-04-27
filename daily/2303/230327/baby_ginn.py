import sys
sys.stdin = open("daily/230327/babygin.txt")

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    c = [0] * 10
    # 리스트 숫자를 c에 넣어줌
    for i in lst:
        c[int(i)] += 1 # c의 인덱스 번호에 1더하기

    i = 0
    tri = run = 0
    while i < 10:
        # tri를 조사
        if c[i] >=3:
            c[i] -= 3
            tri += 1
            continue
        # run을 조사
        if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2: print("Baby Gin")
    else: print("Lose")


