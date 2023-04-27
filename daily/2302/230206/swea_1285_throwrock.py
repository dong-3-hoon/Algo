T = int(input())

for tc in range(1, T+1):
    person = int(input())
    per = 0
    llst = []
    lst = list(map(float, input().split()))
    min_ = 9999999
    for i in lst:
        cnt =abs(0-i)
        if cnt<=min_:
            min_ = cnt
            llst.append(cnt)
    print(f'#{tc} {llst.count(min_)}')