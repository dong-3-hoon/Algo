A = input().upper()
dic = {}
m = 0

ans = ""
for i in A:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic:
    if dic[i] == m:
        ans = "?"
    if dic[i] > m:
        m = dic[i]
        ans = i

print(ans)
