def fact(num):
    if num==0:
        return 1
    else:
        num*=fact(num-1)
        return num
num=int(input())

print(fact(num))