def fibonacci(n):
    if fibo[n] == [0,0]:
        if fibo[n-1] ==[0,0]:
            fibonacci(n-1)
        fibo[n] = [x+y for x,y in zip(fibo[n-1], fibo[n-2])]
        return fibo[n]
    else:
        return fibo[n]
T=int(input())

for test_case in range(1, T+1):
    n=int(input())
    fibo=[]
    for i in range(41):
        line=[]
        for j in range(2):
            line.append(0)
        fibo.append(line)
    fibo[0]=[1,0]
    fibo[1]=[0,1]
    print(fibonacci(n)[0], fibonacci(n)[1])