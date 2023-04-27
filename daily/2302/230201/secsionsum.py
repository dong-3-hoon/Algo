"""T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    lst = list(map(int, input().split()))
    llst = []
    for j in range(A-B+1):  # 계산값을 구함
        cnt = 0
        for i in range(j, j+B):
            cnt += lst[i]
        llst.append(cnt)
    for i in range(len(llst)):  # bubble sort 로 정렬
        for j in range(len(llst)):
            if i != j and llst[i] > llst[j]:
                llst[i], llst[j] = llst[j], llst[i]
    print(f'#{tc} {llst[0]-llst[-1]}')"""

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    lst = list(map(int, input().split()))
    min_ = 99999999
    max_ = 0
    for j in range(A-B+1):  # 계산값을 구함
        cnt = 0
        for i in range(j, j+B):
            cnt += lst[i]
        if cnt < min_:
            min_ = cnt
        if cnt > max_:
            max_ = cnt
    print(max_ - min_)