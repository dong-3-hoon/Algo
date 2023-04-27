L = int(input())
lst = input()
cnt = 0
for i in range(len(lst)):
    cnt += (ord(lst[i]) - 96) * 31**i
print(cnt % 1234567891)

# https://velog.io/@dongkan9/15829%EB%B2%88-Hashing-Python
