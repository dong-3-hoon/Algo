num = int(input())
cnt = [[]*num for _ in range(num)]
for i in range(1, 10):
    cnt[0].append(i)
stk = 0
while True:
    if stk==num-1:
        break
    if stk == 0:
        for i in cnt[stk]:
            if i == 1:
                cnt[stk+1].append(0)
                cnt[stk+1].append(2)
            elif i == 2:
                cnt[stk+1].append(1)
                cnt[stk+1].append(3)
            elif i == 3:
                cnt[stk+1].append(2)
                cnt[stk+1].append(4)
            elif i == 4:
                cnt[stk+1].append(3)
                cnt[stk+1].append(5)
            elif i == 5:
                cnt[stk+1].append(4)
                cnt[stk+1].append(6)
            elif i == 6:
                cnt[stk+1].append(5)
                cnt[stk+1].append(7)
            elif i == 7:
                cnt[stk+1].append(6)
                cnt[stk+1].append(8)
            elif i == 8:
                cnt[stk+1].append(7)
                cnt[stk+1].append(9)
            elif i == 9:
                cnt[stk+1].append(8)
    else:
        for i in cnt[stk]:
            if i == 0:
                cnt[stk+1].append(1)
            if i == 1:
                cnt[stk+1].append(0)
                cnt[stk+1].append(2)
            elif i == 2:
                cnt[stk+1].append(1)
                cnt[stk+1].append(3)
            elif i == 3:
                cnt[stk+1].append(2)
                cnt[stk+1].append(4)
            elif i == 4:
                cnt[stk+1].append(3)
                cnt[stk+1].append(5)
            elif i == 5:
                cnt[stk+1].append(4)
                cnt[stk+1].append(6)
            elif i == 6:
                cnt[stk+1].append(5)
                cnt[stk+1].append(7)
            elif i == 7:
                cnt[stk+1].append(6)
                cnt[stk+1].append(8)
            elif i == 8:
                cnt[stk+1].append(7)
                cnt[stk+1].append(9)
            elif i == 9:
                cnt[stk+1].append(8)
    stk += 1
print(len(cnt[num-1]))