import sys

sys.stdin = open("daily/230214/1219.txt")
# from pprint import pprint


def dfs(s, V):
    # v 대신 end를 하면 end가 v보다 큰 경우에 안 돌아간다.
    visited = [0] * (V + 1)
    stack = []
    i = s
    visited[i] = 1
    while True:
        for w in range(1, V + 1):
            # 길이 있고, 방문한 적이 없을 경우
            if adj[i][w] == 1 and visited[w] == 0:
                # stack에 추가하고 위치 조정 및 방문에 추가
                stack.append(i)
                i = w
                visited[w] = 1
        else:
            # stack에 원소가 있는 경우 pop
            if stack:
                i = stack.pop()
            # 없으면 반복 종료
            else:
                break
    # 목적지에 방문한 적이 있으면 1 리턴
    if visited[end] == 1:
        return 1
    return 0


while True:
    # tc 및 길이 구하기
    case, leng = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[0] * (100) for i in range(100)]
    # 방향 받은것을 2씩 건너뛰어가면서 adj에 길 생성
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i + 1]] = 1
    # 시작, 끝, 노드 수
    s, end, V = 0, 99, 99
    print(f"#{case} {dfs(s, V)}")
    if case == 10:
        break
