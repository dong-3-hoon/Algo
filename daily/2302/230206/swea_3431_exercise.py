T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    D = 0
    if A<=C<=B:
        pass
    elif C<A:
        D = A-C
    else:
        D = -1
    print(f'#{tc} {D}')