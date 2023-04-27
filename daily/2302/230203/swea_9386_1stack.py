T = int(input())

for tc in range(1, T+1):
    num = int(input())
    num_str = list(map(int, input()))
    stk = 0
    max_stk = []
    for i in num_str:
        if i == 1:
            stk += 1
            max_stk.append(stk)
        else:
            stk = 0
    print(f'#{tc} {max(max_stk)}')