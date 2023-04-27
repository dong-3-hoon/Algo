T = int(input())

for tc in range(1, T+1):
    times24 = list(i for i in range(24))
    a, b = map(int, input().split())
    c = a + b
    if c >23:
        c -= 24
    print(f'#{tc} {times24[c]}')