def word(maap, word_num,x,y):

    print('hihi')
array_num, word_num=map(int, input().split())
x,y=0,0
maap=[]
stk=[]
for i in range(array_num): #맵 생성
    stk=list(map(int, input().split()))
    maap.append(stk)
    stk=[]

if maap[x][y]==1:
    word(maap, word_num, x,y)