import sys
sys.stdin = open('daily/230210/9489_.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    m_cnt = 0
    for x in range(N):
        cnt = 0
        for y in range(M):
            if arr[x][y] == '1':
                cnt += 1
            else:
                cnt = 0
            if cnt>m_cnt:
                m_cnt = cnt
    for x in range(M):
        cnt = 0
        for y in range(N):
            if arr[y][x] == '1':
                cnt += 1
            else:
                cnt = 0
            if cnt>m_cnt:
                m_cnt = cnt
    print(f'#{tc} {m_cnt}')