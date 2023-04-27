T = int(input())

for tc in range(1, 1+T):
    qksqkr = int(input())
    ansstr = ''
    for qks in range(qksqkr):
        a, b = map(str, input().split())
        ansstr += a*(int(b))
    print(f'#{tc}')
    for i in range(1, len(ansstr)+1):
        if i % 10 == 0 and i != 0:
            print(ansstr[i-1])
        else:
            print(ansstr[i-1], end = '')
    print()
