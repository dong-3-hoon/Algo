def w(a,b,c,lst): #리스트 제작 함수
    if a<=0 or b<=0 or c<=0:
        lst[a][b][c]=1
    elif a<b and b<c:
        lst[a][b][c] = lst[a][b][c-1] + lst[a][b-1][c-1] - lst[a][b-1][c]
    else:
        lst[a][b][c] = lst[a-1][b][c] + lst[a-1][b-1][c] + lst[a-1][b][c-1] -lst[a-1][b-1][c-1]
while True:
    oria, orib, oric =map(int, input().split())
    a, b, c=oria, orib, oric
    lst = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
    if a==b==c==-1:
        break
    if a>20:
        a=20
    if b>20:
        b=20
    if c>20:
        c=20
    if a<0:
        a=0
    if b<0:
        b=0
    if c<0:
        c=0
    for i in range(21):
        for j in range(21):
            for k in range(21):
                w(i, j, k, lst)
    print(f'w({oria}, {orib}, {oric}) = {lst[a][b][c]}')