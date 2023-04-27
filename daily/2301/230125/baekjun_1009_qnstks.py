import sys

T = int(input())
for test_case in range(T):
    num1, num2 = map(int, sys.stdin.readline().split())
    array2=[2, 4, 6, 8]
    array3=[3, 9, 1, 7]
    array4=[4, 6]
    array7=[7, 9, 3, 1]
    array8=[8, 4, 2, 6]
    array9=[9, 1]
    if num1==1:
        print(1)
    elif num1==2:
        print(array2[num2%4])
    elif num1==3:
        print(array3[num2%4])
    elif num1==4:
        print(array4[num2%2])
    elif num1==5:
        print(5)
    elif num1==6:
        print(6)
    elif num1==7:
        print(array7[num2%4])
    elif num1==8:
        print(array8[num2%4])
    elif num1==9:
        print(array9[num2%2])
    elif num1==10:
        print(10)