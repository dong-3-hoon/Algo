T = int(input())
for tc in range(1, T+1):
    lent = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * (max(lst)+1)
    ans = [0] * len(lst)
    for i in lst:
        cnt[i] += 1
    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]
    for k in range(len(lst)-1, -1, -1):
        cnt[lst[k]] -= 1
        ans[cnt[lst[k]]] = lst[k]
    print(f'#{tc} {" ".join(map(str, ans))}')
