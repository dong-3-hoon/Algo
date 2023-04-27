tc = 1
while tc < 11:
    # counting sort 내림차순
    dump = int(input())
    data = list(map(int, input().split()))
    while dump > 0:
        max_, min_ = 0, 999999
        max_cnt, min_cnt = 0, 0
        for i in range(len(data)):
            # 최댓값, 최솟값을 저장
            if data[i] > max_:
                max_ = data[i]
                max_cnt = i
            if data[i] < min_:
                min_ = data[i]
                min_cnt = i
        data[max_cnt] -= 1
        data[min_cnt] += 1
        dump -= 1
    max_, min_ = 0, 999999
    for i in range(len(data)):
        if data[i] > max_:
            max_ = data[i]
        if data[i] < min_:
            min_ = data[i]
    print(f'#{tc} {max_-min_}')
    tc += 1