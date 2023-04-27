T = int(input())
"""
4
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
5
1 2 3 1 2
"""
for tc in range(1, T+1):
    carrot = int(input())
    lst = list(map(int, input().split()))
    out = 1
    cnt = [1]
    for i in range(carrot):
        if i == carrot-1:
            continue
        else:
            if lst[i] == lst[i+1] - 1:
                out += 1
                cnt.append(out)
            else:
                out = 1
    print(f'#{tc} {max(cnt)}')