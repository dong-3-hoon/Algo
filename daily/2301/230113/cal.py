while True:
    lst=input('숫자와 연산자 사이에 스페이스 눌러주세요:').split()
    result=0
    if lst[-1] == '+' or lst[-1] == '-' or lst[-1] == '*' or lst[-1] =='/':
        print('연산자는 맨 마지막에 올 수 없습니다.')
        break

    for i in range(len(lst)):#리스트 내 숫자를 int형으로 바꿔줌
        if lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] =='/':
            pass
        else:
            lst[i]=float(lst[i])
    #순서대로 하는 코드
    
    for i in range(len(lst)):
        print(i, lst[i])
        if i==0:
            result+=lst[i]
            print(i, lst[i])
        elif i%2!=0:#연산자 파트
            print(i, 'hi')
        else: #숫자 파트
            if lst[i-1]=='+':
                result+=lst[i]
            elif lst[i-1]=='-':
                result-=lst[i]
            elif lst[i-1]=='*':
                result*=lst[i]
            elif lst[i-1]=='/':
                result/=lst[i]
    
    '''
    for i in range(len(lst)):
        if i == '*':
            skt=lst[i-1]*lst[i+1]
            real.append(stk)
        if i == '/':
            stk=lst[i-1]/lst[i+1]
            real.append(stk)
        if lst[i-1]=='*' or lst[i]
        else:
            real.append(lst[i])
    '''
    print(result)
    break