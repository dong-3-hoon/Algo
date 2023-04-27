import sys
sys.stdin = open('daily/230210/4751.txt')
from pprint import pprint

T = int(input())
def first(strr):
    first = '.'
    for i in range(len(strr)):
        first += '.#..'
    return first
def second(strr):
    second = '.'
    for i in range(len(strr)*2):
        second += '#.'
    return second
def dasol(strr):
    lst = '#'
    for i in range(len(strr)):
        lst += '.'
        lst += strr[i]
        lst += '.#'
    return lst
for tc in range(1, T+1):
    strr = input()
    lst1 = first(strr)
    lst3 = second(strr)
    lst2 = dasol(strr)
    print(lst1)
    print(lst3)
    print(lst2)
    print(lst3)
    print(lst1)