import sys

from pprint import pprint

sys.stdin = open("daily/230228/1967.txt")


n = int(input())
max_s = 0
stk = 0
tree = [list(map(int, input().split())) for _ in range(n - 1)]
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(tree)-1):
    arr[tree[i][0]][tree[i][1]] = tree[i][2]
    arr[tree[i][1]][tree[i][0]] = tree[i][2]
pprint(arr)
