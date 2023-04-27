N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(input())
for i in range(M):
    a = input()
    if 65<=ord(a[0])<=122:
        print(int(lst.index(a))+1)
    else:
        print(lst[int(a)-1])