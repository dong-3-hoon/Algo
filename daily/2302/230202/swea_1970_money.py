A = int(input())
for tc in range(1, A+1):
    T = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * len(lst)
    for i in range(len(lst)):
        if T//lst[i] > 0:
            cnt[i] += T//lst[i]
            T = T % lst[i]
    print(f"#{tc}")
    print(" ".join(map(str, cnt)))