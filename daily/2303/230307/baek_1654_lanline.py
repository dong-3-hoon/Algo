a, b = map(int, input().split())
lst = []
for i in range(a):
    lst.append(int(input()))
ans = []
cnt = b - 1
for k in range(b - 1, b + 1):
    stk = 0
    for i in lst:
        stk += int(i) // cnt
    if stk < b:
        break
    cnt += 1
print(cnt - 1)
