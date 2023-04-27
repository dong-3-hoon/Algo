M = int(input())
S = []
lst = []
for i in range(M):
    a = input()
    lst.append(a)
for i in lst:
    if ' ' in i:
        k, j = map(str, i.split())
        if k == 'add' and j not in S:
            S.append(j)
        elif k =='check':
            if j in S:
                print(1)
            else:
                print(0)
        elif k =='remove' and j in S:
            S.remove(j)
        elif k == 'toggle':
            if j in S:
                S.remove(j)
            else:
                S.append(j)
    else:
        if i == 'all':
            S=[]
            for k in range(1, 21):
                S.append(k)
        else: # empty
            S=[]