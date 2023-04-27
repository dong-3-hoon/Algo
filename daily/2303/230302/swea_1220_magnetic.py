import sys

# from pprint import pprint

sys.stdin = open("daily/230302/1220.txt")
tc = 1

while tc < 11:
    num = int(input())
    cnt = 0
    lst = [0] * num
    arr = [list(map(int, input().split())) for _ in range(num)]
    # 세로 기준으로 탐색하며 S극에 사라지는 N 자성체 삭제, S 자성체를 만나면 break
    for i in range(num):
        for j in range(num):
            if arr[j][i] == 1:
                break
            if arr[j][i] == 2:
                arr[j][i] = 0
    # 아래 방향부터 탐색하며 N극에 사라지는 S 자성체 삭제, N 자성체를 만나면 break
    for i in range(num):
        for j in range(num - 1, -1, -1):
            if arr[j][i] == 2:
                break
            if arr[j][i] == 1:
                arr[j][i] = 0
    # 교착 상태 cnt
    for i in range(num):
        for j in range(num):
            # 현재 N 자성체를 처음 만났을 때
            if cnt == 0 and arr[j][i] == 1:
                cnt = 1
            # N 자성체를 만난 이후 S자성체를 만나면
            if cnt == 1 and arr[j][i] == 2:
                lst[j] += 1
                cnt = 0
    print(f"#{tc} {sum(lst)}")
    tc += 1
