T = int(input())

for tc in range(T):
    ryux, ryuy, r1, baekx, baeky, r2 = map(int, input().split())
    ryu_baek = ((ryux-baekx)**2+(ryuy-baeky)**2)**(1/2)
    if r1>r2:
        bigr=r1
        smallr=r2
    elif r1 == r2:
        bigr=r1
        smallr=r2
    else:
        bigr=r2
        smallr=r1
    
    if bigr-smallr < ryu_baek < bigr + smallr:
        print(2)
    elif ryu_baek == bigr+smallr:
        print(1)
    elif ryu_baek == bigr - smallr and ryu_baek != 0:
        print(1)
    elif ryu_baek < bigr - smallr:
        print(0)
    elif ryu_baek > bigr + smallr:
        print(0)
    elif ryu_baek == 0 and bigr == smallr:
        print(-1)