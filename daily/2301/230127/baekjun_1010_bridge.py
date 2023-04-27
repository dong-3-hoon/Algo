def fact(num):
    if num==0:
        return 1
    else:
        num*=fact(num-1)
        return num

T = int(input())
for testcase in range(T):
    num1, num2 = map(int, input().split())
    if num1==num2:
        print(1)
    elif num1==0 or num2==0:
        print(0)
    else:
        under=fact(num1)
        mid=fact(num2-num1)
        upper=fact(num2)
        print(upper//(under*mid))