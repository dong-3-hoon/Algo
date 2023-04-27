import sys
sys.stdin = open("daily/230327/1238.txt")
def bfs(s):
    q = []
    v = [0] * 101
    q.append(s)
    v[s] = 1
    ans = s # 리턴할 노드 번호
    while q:
        c= q.pop(0)
        # 더 늦게 연락받거나 동시에 최종연락이면 큰 값
        if v[ans] < v[c] or (v[ans]==v[c]and ans<c):
            ans = c
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] = v[c]+1
    return ans

T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
            p, c = lst[i], lst[i+1]
            adj[p].append(c)

    ans = bfs(S)
    print(f'#{tc} {ans}')
    tc += 1