import sys

# from pprint import pprint
sys.stdin = open("daily/230221/16639.txt")


# G: 그래프 정보, v: 시작 정점 번호, n: 정점의 개수
def bfs(G, S, n, L):
    # 방문 배열(중복 탐색 방지)
    visited = [0] * (n + 1)
    # 큐 생성
    q = []
    cnt = 0
    # 시작점을 큐에 넣은 상태로 반복 시작
    q.append(S)
    visited[S] = 1
    while q:  # q가 비어있지 않는 동안 반복
        size = len(q)
        cnt += 1
        # 연결된 노드의 길이만큼 반복
        for _ in range(size):
            t = q.pop(0)
            # 현재 정점 t에 연결된 모든 정점 i를 탐색
            for i in G[t]:
                # i 번 정점 방문 x 시 방문
                if not visited[i]:
                    # 다음에 방문하기 위해 큐에 넣고
                    q.append(i)
                    # 방문 처리
                    visited[i] = 1
            # 목적지 도착 시 리턴
            if visited[L] == 1:
                return cnt
    # 목적지 도착 못하면 0 리턴
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for i in range(E):
        start, to = map(int, input().split())
        G[start].append(to)
        G[to].append(start)
    S, L = map(int, input().split())
    k = bfs(G, S, V, L)
    print(f"#{tc} {k}")
