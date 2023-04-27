T = int(input())

lst = [list(map(int, input().split())) for _ in range(T)]
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(len(lst)):
    for j in range(lst[i][0], lst[i][0]+10):
        for k in range(lst[i][1], lst[i][1]+10):
            arr[j][k] = 1
for i in range(100):
    for j in range(100):
        if 0<=i-1<100 and 0<=j-1<100:
            if arr[i][j-1] == 0 and arr[i][j] == 1:
                cnt += 1
            if arr[i-1][j] == 0 and arr[i][j] == 1:
                cnt += 1
for i in range(100, -1, -1):
    for j in range(100, -1, -1):
        if 0<=i+1<100 and 0<=j+1<100:
            if arr[i][j+1] == 0 and arr[i][j] == 1:
                cnt += 1
            if arr[i+1][j] == 0 and arr[i][j] == 1:
                cnt += 1
print(cnt)