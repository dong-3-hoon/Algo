import sys
sys.stdin = open('daily/230208/1221.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    t, num = map(str, input().split())
    lst = list(map(str, input().split()))
    ans = []
    dic_cnt = {}
    dic = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    for i in lst:
        dic[i] += 1
    for i in dic:
        for j in range(dic[i]):
            ans.append(i)
    print(f'#{tc}')
    print(*ans)