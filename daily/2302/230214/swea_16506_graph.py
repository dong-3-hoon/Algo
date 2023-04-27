import sys

sys.stdin = open("daily/230214/16506.txt")
# from pprint import pprint


def dfs(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s
    visited[i] = 1
    while True:
        for w in range(1, V + 1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                if visited[end] == 1:
                    return 1
                else:
                    break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return 0


T = int(input())

for tc in range(1, T + 1):
    # s 간선 수, V 노드
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for i in range(V + 1)]
    for i in range(E):
        st, to = map(int, input().split())
        adj[st][to] = 1
    s, end = map(int, input().split())
    print(f"#{tc} {dfs(s, V)}")
