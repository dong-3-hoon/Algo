A, B, V = map(int, input().split())
'''
cnt = 1
now = 0
while True:
    now += A
    if now>=V:
        break
    now -= A
    now += A-B
    cnt += 1
print(cnt)
'''

K =(V-B)/(A-B)
if K == int(K):
    print(int(K))
else:
    print(int(K)+1)

# https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4