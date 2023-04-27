def bfs(si, sj, ei, ej):
    # queue 생성
    q =[]
    v = [[0]*M for _ in range(N)]
    q.append((si, sj))
    # q 초기 데이터 삽입, v[si][sj] = 1
    v[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        # 정답 처리
        if (ci, cj) == (ei, ej):
            return v[ei][ej]
        # 사방향 탐색 arr == 1 and visited == 0, 범위 내
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <=ni<N and 0<=nj<M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
# bfs(si, sj, ei, ej)
ans = bfs(0, 0, N-1, M-1)
print(ans)