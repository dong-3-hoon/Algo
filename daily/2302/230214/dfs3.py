def dfs(s, V):
    visited = [0] * (V + 1)
    stack = []
    # 현재 방문한 정점을 i
    i = s
    visited[i] = 1
    print(node[i])
    while True:
        # 현재 정점 i 에서 탐색할 수 있는 다음 정점 w 에 대해서
        # w로 가는 길이 있고, w를 방문한적이 없다면 w 방문
        for w in range(1, V + 1):
            if adj[i][w] == 1 and visited[w] == 0:
                # w는 길이 있으니까 현재 위치 i를 스택에 저장
                stack.append(i)
                # 현재 위치 i를 다음위치 w로 변경
                i = w
                print(node[i])
                # w는 방문 했다 라고 표시
                visited[w] = 1
                # 현재 위치 i에서 더 확인할 필요가 없음
                break  # ################################여기서 왜 포문이 안끝남???????????
        # 내가 i에서 탐색을 해봤는데 더이상 탐색할 정점이 없다.
        else:
            # 내가 최근에 방문했던 정점을 스택에 넣어놓았음
            # 하나 꺼내서 그 위치로 돌아감
            if stack:  # 스택이 비어있으면 false취급
                i = stack.pop()
            # 스택이 비어있으면 탐색 종료
            else:
                break
    # 함수 종료 전에 할 일
    return


V, E = map(int, input().split())
adj = [[0] * (V + 1) for i in range(V + 1)]
node = ["", "1", "2", "3", "4", "5", "6", "7"]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프만 아래 추가
    adj[to][start] = 1

"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""
dfs(1, 7)
