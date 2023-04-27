cnt0=0
cnt1=0
def fibonacci(n):
    global cnt0
    global cnt1
    if n==0:
        cnt0+=1
        return 0
    elif n==1:
        cnt1+=1
        return 1
    else:
        return fibonacci(n-2)+fibonacci((n-1))
T=int(input())

for test_case in range(1, T+1):
    n=int(input())

    fibonacci(n)
    print(cnt0, cnt1)
    cnt0=0
    cnt1=0
    