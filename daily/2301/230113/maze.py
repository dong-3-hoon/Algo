#탐색 함수
cnt=0
def search(maze, x, y):
    global ans
    if maze[x][y]=='3':
        ans=1
    maze[x][y]=2
    if maze[x+1][y]=='0' or maze[x+1][y]=='3':
        search(maze, x+1, y)
    if maze[x][y+1]=='0' or maze[x][y+1]=='3':
        search(maze, x, y+1)
    if maze[x-1][y]=='0' or maze[x-1][y]=='3':
        search(maze, x-1, y)
    if maze[x][y-1]=='0' or maze[x][y-1]=='3':
        search(maze, x, y-1)
while True:
    ans=0
    T=int(input())
    maze=[]
    myx=0
    myy=0
    answer=0
    for i in range(16):#미로 생성
        X=input()
        lst =[]
        for j in X:
            lst.append(j)
        maze.append(lst)

    for y in range(16):#현재 위치 탐색
        for x in range(16):
            if maze[x][y]=='2':
                myx=x
                myy=y
    search(maze, myx, myy)

    print(f"#{T} {ans}")
    cnt+=1
    if cnt==10:
        break