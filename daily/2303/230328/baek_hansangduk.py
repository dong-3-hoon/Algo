import sys
from collections import deque
import sys
sys.stdin = open("daily/230328/2842.txt")
def solution():
    input = sys.stdin.readline
    N = int(input()) 
    board = [list(map(str, input())) for _ in range(N)] #상덕이가 움직일 곳
    HEIGHT = [list(map(int, input().split())) for _ in range(N)] # 지역의 고도
    # 8방향 탐색
    moves = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    houses = 0
    heights = []
    
    #시작위치와 집의 개수를 파악한다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'P':
                sx, sy = i, j
            if board[i][j] == 'K':
                houses += 1
            heights.append(HEIGHT[i][j])
    # 중복이 없는 정렬된 1차원 배열 - 높이순 정렬
    heights = sorted(set(heights))
    left, right = 0, 0
    # 양의 무한대 선언 - 최대값을 잡기 위함인듯
    ans = float('inf')
    while left < len(heights):
        #left, right를 움직이면서 탐색해준다.
        visit = [[False] * N for _ in range(N)] 
        # q 선언
        q = deque()
        #시작점의 고도가 범위안에 들어와야한다. - 방문해야 하는 최소 높이 ~ 최대 높이
        if heights[left] <= HEIGHT[sx][sy] <= heights[right]: 
            visit[sx][sy] = True
            q.append((sx, sy))

        cnt = 0 # 방문한 집의 개수
        while q:
            r, c = q.popleft()
            for dr, dc in moves:
                # 8방향 탐색
                nr, nc = r + dr, c + dc
                # 예외처리
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    continue
                # 새로 방문한 곳의 고도가 범위안에 포함되면
                if not visit[nr][nc] and heights[left] <= HEIGHT[nr][nc] <= heights[right]: 
                    # 집 도착 시 집 개수 증가
                    if board[nr][nc] == 'K': cnt += 1
                    # 방문 표시
                    visit[nr][nc] = True
                    q.append((nr, nc))
                    

        if cnt == houses: # 집을 모두 방문했다면
            ans = min(ans, heights[right] - heights[left]) #정답 갱신
            left += 1 # 포인터를 왼쪽으로 옮겨서 더 고도의 범위를 좁혀준다.(탐색가능한 최소값을 찾을 것)
        elif right + 1 < len(heights): # 아직 남아있는 최대 고도가 있을 때
            right += 1 # 포인터를 오른쪽으로 옮겨서 더 고도의 범위를 넓혀준다.
        else: # 방문 못햇다면
            break 
    print(ans)

solution()

# https://butter-shower.tistory.com/226
# https://www.acmicpc.net/problem/2842