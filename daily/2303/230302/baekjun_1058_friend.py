import sys

# from pprint import pprint

sys.stdin = open("daily/230302/1058.txt")

T = int(input())

for tc in range(1, T + 1):
    dim = int(input())
    arr = [list(input()) for _ in range(dim)]
    m_cnt = 0
    for i in range(dim):
        cnt = 0
        for j in range(dim):
            if arr[i][j] == "Y":
                cnt += 1
                for k in range(dim):
                    if arr[j][k] == "Y":
                        cnt += 1
        if m_cnt < cnt:
            m_cnt = cnt
    print(cnt)
