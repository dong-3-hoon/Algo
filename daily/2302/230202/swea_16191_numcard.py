T = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = list(map(str, input()))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    cnt = [0] * (max(lst)+1)
    for i in range(len(lst)):
        cnt[lst[i]] += 1
    cnt.reverse()
    print(f'#{tc} {len(cnt)-cnt.index(max(cnt))-1} {max(cnt)}')
