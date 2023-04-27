from collections import deque
def bfs():
    # [1] q생성, v[]생성
    q = deque()
    v = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1: # 익은토마토
                q.append((i,j))
                v[i][j]=1
            elif arr[i][j]==0: # 안익은토마토
                cnt += 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
                cnt -= 1    # 안익은 토마토 1개 익음

    if cnt==0:              # 모든 토마토 익었음
        return v[ci][cj]-1
    else:
        return -1

M, N= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
print(ans)