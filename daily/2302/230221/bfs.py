# G: 그래프 정보, v: 시작 정점 번호, n: 정점의 개수
def bfs(G, v, n):
    # 방문 배열(중복 탐색 방지)
    visited = [0] * (n + 1)
    # 큐 생성
    q = []
    # 시작점을 큐에 넣은 상태로 반복 시작
    q.append(v)
    visited[v] = 1
    while q:  # q가 비어있지 않는 동안 반복
        t = q.pop(0)
        print(node[t])
        # 현재 정점 t에 연결된 모든 정점 i를 탐색
        for i in G[t]:
            # i 번 정점 방문 x 시 방문
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 넣고
                q.append(i)
                # 방문 처리
                visited[i] = 1


#        0    1    2    3    4    5    6    7    8    9
node = ["x", "A", "B", "C", "D", "E", "F", "G", "H", "I"]


"""
1. 그래프의 정보가 주어지는데 어떻게 처리할거냐
정점의 개수 V = 9
간선의 개수 E = 8
9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9
"""
"""
연습 문제3
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
"""
V, E = map(int, input().split())
"""
인접 리스트
G[A] = [B, C, D]
G[B] = [A, E, F]
"""
G = [[] for _ in range(V + 1)]
# 인접 리스트 생성
for i in range(E):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

print(G)
bfs(G, 1, V)
