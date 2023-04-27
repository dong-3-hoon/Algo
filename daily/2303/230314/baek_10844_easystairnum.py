num = int(input())
cnt = []
stk = '1'
for i in range(num-1):
    stk += '0'
stk = int(stk)
while True:
    if len(k) > num:
        break
    k = str(stk)
    hihi = 0
    for i in range(len(k)):
        if i<len(k)-1 and (int(k[i])+1 == int(k[i+1]) or int(k[i])-1 == int(k[i+1])):
            hihi += 1
    if hihi == num-1:
        cnt.append(stk)
    stk += 1
print(cnt)
print(len(cnt))
