T = int(input())

for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    cnt = 0
    ans = []
    now = 1
    while True:
        print(ans)
        if now > 20:
            break
        if now == 1:
            ans.append(lst[now])
        else:
            ans.append(lst[now])
            for i in range(now, -1, -1):
                if ans[i] < ans[i - 1]:
                    ans[i], ans[i - 1] = ans[i - 1], ans[i]
                    cnt += 1
        now += 1
    print(f"{tc} {cnt}")
