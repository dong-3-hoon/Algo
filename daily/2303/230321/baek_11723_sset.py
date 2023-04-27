M = int(input())
S = []
for i in range(21):
    S.append(0)
lst = []
for i in range(M):
    a = input()
    lst.append(a)

for i in lst:
    if ' ' in i:
        k, j = map(str, i.split())
        j = int(j)
        if k == 'add':
            S[j] = 1
        elif k =='check':
            if S[j] == 1:
                print(1)
            else:
                print(0)
        elif k =='remove':
            S[j] = 0
        elif k == 'toggle':
            if S[j] == 1:
                S[j] = 0
            else:
                S[j] = 1
    else:
        if i == 'all':
            S=[]
            for k in range(21):
                S.append(1)
        else: # empty
            S=[]
            for k in range(21):
                S.append(0)