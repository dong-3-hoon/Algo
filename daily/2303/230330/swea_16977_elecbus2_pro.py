import sys
sys.stdin = open("daily/230330/16977.txt")
T = int(input())
 
 
# 현재 정류장 위치 : idx
# 충전 횟수 : cnt
def backtracking(idx, cnt):
    global min_v
 
    # 가지 치기
    # 현재까지 내가 충전한 횟수가 min_v 보다 크면 더이상 진행 할 필요가 없다
    if cnt >= min_v:
        return
 
    # 종료 조건
    if idx >= n - 1:
        min_v = min(min_v, cnt)
        return
 
    # 재귀 호출
    # 현재 위치에서 갈수 있는곳 골라서 가기
    # 현재 위치 idx에서 갈수 있는 곳 : idx + 1 ~ idx + bus_stop[idx] 까지 갈수 있음
    for i in range(1, bus_stop[idx] + 1):
        backtracking(idx + i, cnt + 1)
 
 
for tc in range(1, T + 1):
    n, *bus_stop = map(int, input().split())
    bus_stop += [0]
 
    # print(n, bus_stop)
    # 최소 충전 횟수
    min_v = 101
 
    backtracking(0, -1)
 
    print(f"#{tc} {min_v}")