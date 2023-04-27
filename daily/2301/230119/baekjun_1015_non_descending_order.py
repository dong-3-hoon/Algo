#ndo란 주어진 리스트에서 작은 값대로 return 하는 리스트를 생성해줌

a=int(input())
b=list(map(int, input().split()))
lst=[]
for i in range(a):
    cnt=0
    for j in range(a):
        if i != j:
            if b[i]>b[j]:
                cnt+=1
    lst.append(cnt)
    #print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j and lst[i]==lst[j]:
            lst[j]+=1
for i in lst:
    print(i, end=' ')
    '''
# a=3
# b=[2, 3, 1]
# NDO(a, b)
#1 2 0
a=4
b=[2, 1, 3, 1]
#NDO(a, b)
#2 0 3 1
a=8
#b=[4, 1, 6, 1, 3, 6, 1, 4]
NDO(a, b)
#4 0 6 1 3 7 2 5'''