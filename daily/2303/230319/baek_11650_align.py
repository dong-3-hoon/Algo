N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
for i in range(1, N):
    if lst[i][0]<lst[i-1][0]:
        lst[i], lst[i-1] = lst[i-1], lst[i]
for i in range(1, N):
    if lst[i][0] == lst[i-1][0] and lst[i][1]<lst[i-1][1]:
        lst[i], lst[i-1] = lst[i-1], lst[i]
for i in lst:
    for j in i:
        print(j, end=' ')
    print()