import sys

# from pprint import pprint

sys.stdin = open("daily/230221/16674.txt")
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < dim and 0 <= c < dim


# sr : 시작 행
# sc : 시작 열
def bfs(sr, sc):
    visited = [[0] * dim for _ in range(dim)]
    q = []
    q.append((sr, sc))  # 시작점 sr, sc를 큐에 삽입
    visited[sr][sc] = 1
    day = -1
    while q:
        day += 1
        # 원소를 반환하기 전에 현재 단계에서 큐의 원소를 몇개까지 하면 되는지
        size = len(q)
        # 갈림길의 갯수만큼 반복
        for _ in range(size):
            r, c = q.pop(0)  # 큐의 첫번째 원소를 반환
            # 목적지 도착 시 결과값 리턴
            if maze[r][c] == 2:
                return day - 1
            maze[r][c] = 1
            # 현재 위치 r,c 에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 유효한인덱스, 벽이아님, 방문한적도 없음
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))  # 큐에 넣기
                    visited[nr][nc] = 1  # 방문 체크
    return 0


T = int(input())
for tc in range(1, T + 1):
    dim = int(input())
    maze = [list(map(int, input())) for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 3:
                x, y = i, j
    k = bfs(x, y)
    print(f"#{tc} {k}")
