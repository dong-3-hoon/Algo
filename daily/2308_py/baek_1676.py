st = int(input())
num = 1
for i in range(1, st+1):
    num *=i
cnt = 0
gg = str(num)
for i in range(len(gg)-1, -1, -1):
    if gg[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break
