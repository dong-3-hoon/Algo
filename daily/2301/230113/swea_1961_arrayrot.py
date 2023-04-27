def rot90(n, lst):#90도 회전 함수
    lst90=[]
    stk=[]
    for i in range(n):#rotate 90
        for j in range(n-1, -1, -1):
            stk.append(lst[j][i])
        lst90.append(stk)
        stk=[]
    return lst90

def rot180(n, lst):#180도 회전 함수
    lst180=[]+lst
    lst180 = list(reversed(lst180))
    for i in range(n):#rotate180
        lst180[i]=list(reversed(lst180[i]))
    return lst180

#메인
T = int(input())
for test_case in range(1, T + 1):
    lst=[]
    stk=[]
    n=0
    cnt=0
    n=int(input())
    for i in range(n):#기본 배열 생성
        lst.append(list(map(int, input().split())))
    #180도 회전
    lst180=rot180(n, lst)
    #90도 회전
    lst90=rot90(n, lst)
    #270도 회전
    lst270=rot180(n, lst90)
    print("#{0}".format(test_case))
    while True:#출력 함수
        for i in range(n):
            if i==n-1:
                print(f"{lst90[cnt][i]}", end=' ')
            else:
                print(f"{lst90[cnt][i]}", end='')
        for i in range(n):
            if i==n-1:
                print(f"{lst180[cnt][i]}", end=' ')
            else:
                print(f"{lst180[cnt][i]}", end='')
        for i in range(n):
            if i==n-1:
                print(f"{lst270[cnt][i]}")
            else:
                print(f"{lst270[cnt][i]}", end='')
        cnt+=1
        if cnt==n:
            break
            