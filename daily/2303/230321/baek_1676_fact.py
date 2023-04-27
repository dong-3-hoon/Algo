num = int(input())
cnt = 1
for i in range(1, num+1):
    cnt *= i
stk = str(cnt)
hihi = 0
for i in stk[::-1]:
    if i != '0':
        break
    if i == '0':
        hihi += 1
print(hihi)