from pprint import pprint
def bfs(i, j, stk):
    q=[]
    v[i][j] = stk
    q.append((i, j))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<num and 0<=nj<num and v[ni][nj] == 0 and arr[ni][nj] ==1:
                q.append((ni, nj))
                v[ni][nj] = stk


num = int(input())

arr = [list(map(int, input())) for _ in range(num)]
v = [[0] * num for _ in range(num)]
stk = 1
for i in range(num):
    for j in range(num):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i, j, stk)
            stk += 1
stk -= 1
print(stk)
kk = []
for i in range(1, stk+1):
    cnt = 0
    for j in range(num):
        for k in range(num):
            if v[j][k] == i:
                cnt += 1
    kk.append(cnt)
kk.sort()
for i in kk:
    print(i)