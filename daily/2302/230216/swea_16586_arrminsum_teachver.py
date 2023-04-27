import sys

# from pprint import pprint

sys.stdin = open("daily/230216/16586.txt")


# 현재 i 번째 행에 대해서 j 번째 열을 골라서 합을 만들기
def backtracking(i, now_sum):
    global min_sum
    # 가지치기
    if now_sum > min_sum:
        return
    # 종료 조건
    if i == n:
        if now_sum < min_sum:
            min_sum = now_sum
        return
    # 재귀
    # 0 ~ n-1번째 열 중 이전에 고른적이 없는 j열을 선택
    for j in range(n):
        # 고른 적이 없는지 확인
        if not select[j]:
            select[j] = 1
            # j 번째 열을 고르고 합을 구한 다음 다음 행으로 진행
            backtracking(i + 1, now_sum + board[i][j])
            select[j] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    select = [0] * n
    min_sum = 100

    backtracking(0, 0)
    print(f"#{tc} {min_sum}")
