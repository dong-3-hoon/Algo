T = int(input())

for tc in range(1, T+1):
    a = int(input())
    b = int(input())
    lst = []
    for i in range(1, b+1):
        lst.append(i)
    arr = []
    arr.append(lst)
    for i in range(a):
        lst = []
        for j in range(b):
            lst.append(0)
        arr.append(lst)
    for i in range(1, a+1):
        for j in range(b+1):
            for k in range(j):
                arr[i][j-1] += arr[i-1][k]
    print(arr[a][b-1])