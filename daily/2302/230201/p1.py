import sys

sys.stdin = open('input.txt')

#33
N = int(input())
result = 1 if N % 2 else 0
print(f'{result}')