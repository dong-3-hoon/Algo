num1=input()
num2=int(input())
lst=[]
strr=''
for i in num1:
    lst.append(i)
for i in range(10):
    lst[-2]=str(i)
    for j in range(10):
        lst[-1]=str(j)
        for i in lst:
            strr+=i
        if int(strr)%num2==0:
            #여기서 맨 뒷자리 2개만 제거
            print(f'{strr[-2]}{strr[-1]}')
            quit()
        strr=''

