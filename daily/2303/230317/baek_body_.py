num = int(input())
hight = []
weight = []
s_hight=[]
s_weight=[]
body = [0] * (num)
cnt = 1
stk = 0
for i in range(num):
    a, b = map(int, input().split())
    hight.append(a)
    s_hight.append(a)
    weight.append(b)
    s_weight.append(b)
s_hight.sort(reverse=True)
s_weight.sort(reverse=True)
print(s_hight)
for i in range(num):
    print(s_hight[i], s_weight[i])
    print(hight.index(s_hight[i]), weight.index(s_weight[i]))
    if hight.index(s_hight[i])==weight.index(s_weight[i]):
        body[hight.index(s_hight[i])] = cnt
        cnt += 1
print(body)
for i in range(max(body)):
    for j in range(num):
        if i == body[j]:
            
# for i in range(num):
#     for j in range(num):
#         if i != j:
