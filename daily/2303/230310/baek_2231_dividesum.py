num = int(input())
for i in range(num):
    cnt = i
    for j in str(i):
        cnt += int(j)
    if cnt == num:
        print(i)
        break
else:
    print(0)
