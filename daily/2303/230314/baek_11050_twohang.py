N, K = map(int, input().split())
cnt = 1
stk = 1
hoho = 1
for i in range(1, N+1):
    cnt *= i
for j in range(K, 0, -1):
    stk *=j
for k in range(N-K, 0, -1):
    hoho *= k
print(int(cnt/stk/hoho))