import sys

# from pprint import pprint

sys.stdin = open("daily/230301/4613.txt")


# 한 줄에서 흰색이 아닌 부분을 세는 코드
def trans_w(a):
    global N, M
    cnt = 0
    for i in range(M):
        if arr[a][i] != "W":
            cnt += 1
    return cnt


# 한 줄에서 파란색이 아닌 부분을 세는 코드
def trans_b(a):
    global N, M
    cnt = 0
    for i in range(M):
        if arr[a][i] != "B":
            cnt += 1
    return cnt


# 한 줄에서 빨간색이 아닌 부분을 세는 코드
def trans_r(a):
    global N, M
    cnt = 0
    for i in range(M):
        if arr[a][i] != "R":
            cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    stk = []
    # 파란색 줄 갯수
    b_line = 1
    # 파란 줄 시작 지점
    b_start = 1
    while True:
        w_cnt, r_cnt, b_cnt = 0, 0, 0
        # 파란색 끝 지점은 시작 + 줄 갯수
        b_end = b_start + b_line
        # 파란 줄의 갯수가 흰색, 빨간줄 제외 전체이면 break
        if b_line == N - 1:
            break
        # 0~파란 줄 시작까지 흰색 줄 갯수만큼 흰색으로 바꾸는 것을 세는 함수 호출
        for i in range(0, b_start):
            w_cnt += trans_w(i)
        # 파란 줄 시작 ~ 끝까지 바꾸는 것을 세는 함수 호출
        for i in range(b_start, b_end):
            b_cnt += trans_b(i)
        # 파랑 끝 ~ 전체 갯수만큼 빨강 갯수 세는 함수 호출
        for i in range(b_end, N):
            r_cnt += trans_r(i)
        # 각 함수에서 바꿔야 할 총 갯수를 리스트에 저장
        stk.append(w_cnt + r_cnt + b_cnt)
        # 시작을 증가시켜가며 탐방
        b_start += 1
        if b_line == N - 1:
            break
        # 마지막 줄까지 왔다면 다시 처음으로 돌아가고 줄 갯수 증가
        if b_end == N - 1:
            b_line += 1
            b_start = 1
    # 리스트의 최솟값 출력
    print(f"#{tc} {min(stk)}")
