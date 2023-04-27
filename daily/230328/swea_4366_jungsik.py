import sys
sys.stdin = open("daily/230328/4366.txt")
T = int(input())
def change2():
    stk = ''
    cnt = 0
    for i in bi:
        stk += i
    kk = stk[::-1]
    for i in range(len(stk)):
        cnt += int(kk[i])*(2**i)
    b_cor.append(cnt)

def change3():
    global ans
    stk = ''
    cnt = 0
    for i in th:
        stk += i
    kk = stk[::-1]
    for i in range(len(stk)):
        cnt += int(kk[i])*(3**i)
    if cnt in b_cor:
        ans = cnt
for tc in range(1, T+1):
    ans = 0
    b_cor = []
    bi = list(input())
    th = list(input())
    for i in range(len(bi)):
        if bi[i] =='0':
            bi[i] = '1'
            change2()
            bi[i] = '0'
        elif bi[i] == '1':
            bi[i] = '0'
            change2()
            bi[i] = '1'
    for i in range(len(th)):
        if th[i] == '0':
            th[i] = '1'
            change3()
            th[i] = '2'
            change3()
            th[i] = '0'
        elif th[i] == '1':
            th[i] = '2'
            change3()
            th[i] = '0'
            change3()
            th[i] = '1'
        elif th[i] == '2':
            th[i] = '1'
            change3()
            th[i] = '0'
            change3()
            th[i] = '2'
    print(f'#{tc} {ans}')