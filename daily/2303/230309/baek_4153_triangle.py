while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    a = max(lst)
    b = min(lst)
    for i in lst:
        if i != a and i != b:
            c = i
    if c**2 + b**2 == a**2:
        print('right')
    else:
        print('wrong')