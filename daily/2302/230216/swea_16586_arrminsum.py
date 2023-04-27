import sys

# from pprint import pprint

sys.stdin = open("daily/230216/16586.txt")


def backtracking(row, remain):
    global cnt
    # 가지치기
    if sum(ans) > cnt:
        return

    # 종료 조건
    if row == n and remain == 0:
        if sum(ans) < cnt:
            cnt = sum(ans)
        return cnt
    for i in range(n):
        can_place = True

        # 세로에 선택한 숫자가 있는지 검사
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break
        # 놓을 수 있는지 검사
        if can_place:
            # 놓을 수 있으면 현재 위치에 놓고 다음 위치로 이동
            board[row][i] = 1
            ans.append(arr[row][i])
            backtracking(row + 1, remain - 1)
            # 다시 되돌려 놓고 진행 할 수 있도록 해준다
            ans.remove(arr[row][i])
            board[row][i] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 경우의 수 구하기
    cnt = 99999
    ans = []
    arr = []
    for i in range(n):
        lst = list(map(int, input().split()))
        arr.append(lst)
    # 보드 만들기
    board = [[0] * n for i in range(n)]
    backtracking(0, n)
    print(f"#{tc} {cnt}")
