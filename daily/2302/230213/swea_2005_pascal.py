import sys
sys.stdin = open('daily/230213/2005.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    row = int(input())
    print(f'#{tc}')
    for q in range(1, row+1):
        #짝수
        if q % 2 == 0:
            if q == 2:
                pascal2 = [1, 1]
            else:
                for i in range(q):
                    if i == 0:
                        pascal2 = [1]
                    elif i == q - 1:
                        pascal2.append(1)
                    else:
                        pascal2.append(pascal1[i-1]+pascal1[i])
            print(*pascal2)
        #홀수
        else:
            if q == 1:
                pascal1 =[1]
            else:
                for i in range(q):
                    if i == 0:
                        pascal1 = [1]
                    elif i == q - 1:
                        pascal1.append(1)
                    else:
                        pascal1.append(pascal2[i-1]+pascal2[i])
            print(*pascal1)