N = int(input())
lst = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
for i in range(M):
    if find[i] in lst:
        print(1)
    else:
        print(0)
