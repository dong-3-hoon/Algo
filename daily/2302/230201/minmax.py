T = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(f'#{tc} {lst[0]-lst[-1]}')
