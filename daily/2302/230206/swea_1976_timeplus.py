T = int(input())

for tc in range(1, T+1):
    bt, bm, at, am = map(int, input().split())
    time = bt + at
    minute = bm + am
    if minute >= 60:
        time += 1
        minute -= 60
    if time > 12:
        time -= 11
    print(f'#{tc} {time} {minute}')