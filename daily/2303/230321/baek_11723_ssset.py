M = int(input())
S = []
ans = []
for i in range(21):
    S.append(0)
for i in range(M):
    lst = input()
    if ' ' in lst:
        k, j = map(str, lst.split())
        j = int(j)
        if k == 'add':
            S[j] = 1
        elif k =='check':
            if S[j] == 1:
                ans.append(1)
            else:
                ans.append(0)
        elif k =='remove':
            S[j] = 0
        elif k == 'toggle':
            if S[j] == 1:
                S[j] = 0
            else:
                S[j] = 1
    else:
        if lst == 'all':
            S=[]
            for k in range(21):
                S.append(1)
        else: # empty
            S=[]
            for k in range(21):
                S.append(0)
for i in ans:
    print(i)