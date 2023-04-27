array_num, fly_chae=map(int, input().split())
maap=[] #맵 저장
answer=[] #정답 저장
stk=[]#중간과정 저장
now_x, now_y=0,0 #현재 위치
chae_x, chae_y=0,0 #파리채 위치
cnt=0
for i in range(array_num): #맵 생성
    lst=list(map(int, input().split()))
    maap.append(lst)
for x in range(now_x, array_num-fly_chae+1):
    for y in range(now_y, array_num-fly_chae+1):
        for i in range(x, fly_chae+x):
            for j in range(y, fly_chae+y):
                stk.append(maap[i][j])
        answer.append(sum(stk))
        stk=[]
print(max(answer))