import sys

sys.stdin = open("sum.txt")

tc = 1
while tc<11:
    T = int(input())
    arr = []
    for i in range(100):
        lst = list(map(int, input().split()))
        arr.append(lst)
    lst = []
    dx = [1, -1]
    dy = [1, -1]
    #x축 덧셈
    for x in range(100):
        lst.append(sum(arr[x]))
    #y축 덧셈
    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for y in range(100):
        lst.append(sum(arr[y]))
    #대각선 덧셈
    cnt = 0
    for i in range(100):
        cnt += arr[i][i]
    lst.append(cnt)
    cnt = 0
    for j in range(100):
        cnt += arr[j][99-j]
    lst.append(cnt)
    max_cnt = 0
    for i in lst:
        if i > max_cnt:
            max_cnt = i
    print(f'#{tc} {max_cnt}')
    tc += 1