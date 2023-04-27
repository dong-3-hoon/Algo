
def find_cabbage(maap, n, m, cabbage, nowx, nowy, worm):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    if find_cabbage==1 and maap[nowx][nowy]==0:
        worm+=1
    
    return worm
    print('hi')
#T=int(input())
#for test_case in range(T):
loc_cabbage=[] #배추 위치
cnt=[] # 맵 제작용 cnt
maap=[] #맵
nowx=0
nowy=0
worm=0

#맵의 크기와 배추의 갯수 입력
n, m, cabbage=map(int, input().split())

#배추의 위치를 리스트에 저장
for i in range(cabbage): 
    cnt=list(map(int, input().split()))
    loc_cabbage.append(cnt)
loc_cabbage.sort()

#맵 제작
for i in range(n):
    cnt=[]
    for j in range(m):
        if [i, j] in loc_cabbage:#loc_cabbage에 있는 위치라면 1
            cnt.append(1)
        else:
            cnt.append(0)
    maap.append(cnt)

