def bfs(start, end):
    q=[]
    q.append(start)
    v[start] = 1
    while q:
        t = q.pop(0)
        for i in G[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t] + 1

num = int(input())
con = int(input())
hihi = 0
G = [[] for _ in range(num+1)]
v = [0] * (num+1)
for i in range(con):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)
bfs(1, end)
for i in v:
    if i != 0 and i != 1:
        hihi += 1
print(hihi)