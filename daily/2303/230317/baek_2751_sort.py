num = int(input())
lst=[]
cnt = [0] * (num+1)
for i in range(num):
    a = int(input())
    lst.append(a)
for i in range(num):
    cnt[lst[i]] += 1
for i in range(len(cnt)):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)