import sys

# from pprint import pprint

sys.stdin = open("daily/230304/2309.txt")

lst = []
for i in range(9):
    a = int(input())
    lst.append(a)
mafia = sum(lst) - 100
ans = []
a, b = 0, 1
cnt = 0
while True:
    #여기로 올렸는데 통과됨;; 왜일까요?
    cnt = lst[a] + lst[b]
    #더한 값이 100에서 뺀 값과 같다면 나머지를 append해줌
    if cnt == mafia:
        for i in range(9):
            if i == a or i == b:
                continue
            ans.append(lst[i])
        break
    #1씩 증가
    b += 1
    #끝에가면 a증가, b는 a+1
    if b == 9:
        a += 1
        b = a+1
    #원래 여기 있었는데 인덱스에러가 뜸
    #cnt = lst[a] + lst[b]
ans.sort()
for i in ans:
    print(int(i))
