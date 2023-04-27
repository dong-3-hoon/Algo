T = int(input())

lst = [input() for _ in range(T)]
lst.sort()
len_max = 0
a = []
for i in lst:
    if len(i) > len_max:
        len_max = len(i)
for i in range(len_max+1):
    for j in lst:
        if i == len(j) and j not in a:
            a.append(j)
for i in a:
    print(i)
