def vali(): #퀸 정렬 함수
    print('hi')
def dfs(): # 퀸을 백트래킹으로 배치해주는 함수
    if len(lst) == T*2:
        vali()
        return
    for i in range(T):
        lst.append(i)
        dfs()
        lst.pop()
T = int(input())
lst=[]
llst = []
lllst = []
answer=0
dfs()


#00 00 00 00, 00 00 00 01, 00 00 00 02, 00 00 00 03, 00 00 00 04, 00 00 00 10, 
#00 00 00 11, 00 00 00 12, 00 00 00 13, 00 00 00 142