import sys
import heapq

# from pprint import pprint
sys.stdin = open("daily/230223/16719.txt")

T = int(input())

for tc in range(1, T + 1):
    ans = 0
    N = int(input())
    lst = list(map(int, input().split()))
    hq = []
    llst = [0]
    for i in lst:
        heapq.heappush(hq, i)
    for i in hq:
        llst.append(i)
    print(llst)
    now = len(llst)
    print(now)
    while now > 0:
        now = now // 2
        print(llst[now + 1])
