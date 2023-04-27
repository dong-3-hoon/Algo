T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    k = num ** (1 / 3)
    print(int(k))
    if int(k) == k:
        print(int(k))
    else:
        print(-1)
