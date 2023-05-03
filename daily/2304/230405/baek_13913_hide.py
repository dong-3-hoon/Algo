from collections import deque
def bfs(N):
    q=deque([])
    q.append(N)
    while q:
        t = q.popleft()
        k.append(t)
        t1 = 2*t
        t2 = t+1
        t3 = t-1
        if t == M:
            return lst[t]
        if 0<=t1<100001 and (lst[t1] == 0 or lst[t1] == -1):
            lst[t1] = lst[t]+1
            q.append(t1)
        if 0<=t2<100001 and (lst[t2] == 0 or lst[t2] == -1):
            lst[t2] = lst[t]+1
            q.append(t2)
        if 0<=t3<100001 and (lst[t3] == 0 or lst[t3] == -1):
            lst[t3]= lst[t]+1
            q.append(t3)
    return
N, M = map(int, input().split())
k=[]
lst = [0] * 100001
lst[N] = 1
lst[M] = -1
ans = bfs(N)
if ans<=0:
    print(0)
else:
    print(ans-1)
    print(*k)