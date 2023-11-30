T = int(input())
lst = []
new_lst = []
for i in range(T):
    lst.append(input())
lst.sort()
for i in range(51):
    for j in lst:
        if len(j) == i and j not in new_lst:
            new_lst.append(j)
        else:
            pass
for i in new_lst:
    print(i)