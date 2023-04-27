T = int(input())

for tc in range(T):
    x1, y1, x2, y2 = map(str, input().split())
    lst = []
    maap = []
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                lst.append(0)
            else:
                lst.append(1)
        maap.append(lst)
        lst = []
    print(maap)
    a = x1 + y1
    b = x2 + y2
    if a %2 == 0 and b %2 == 0 or a % 2 != 0 and b % 2 != 0:
        print('Impossible')
    else:
        