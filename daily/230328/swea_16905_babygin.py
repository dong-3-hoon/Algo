import sys
sys.stdin = open("daily/230328/16905.txt")

def bg(n):
    if n == 1 and len(p1) >=3:
        p1.sort()
        c = [0] * 12
        for i in p1:
            c[int(i)] += 1 # c의 인덱스 번호에 1더하기
        i = 0
        tri, now = 0, 0
        while i < 10:
            if c[i] >=3:
                c[i] -= 3
                tri += 1
                return 1
            if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1: 
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                now += 1
                return 1
            i += 1
    elif n==2 and len(p2)>= 3:
        p2.sort()
        c = [0] * 12
        for i in p2:
            c[int(i)] += 1 # c의 인덱스 번호에 1더하기
        i = 0
        tri, now = 0, 0
        while i < 10:
            if c[i] >=3:
                c[i] -= 3
                tri += 1
                return 2
            if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1: 
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                now += 1
                return 2
            i += 1
    return 0

T = int(input())

for tc in range(1, T+1):
    ans = 0
    lst = list(map(int, input().split()))
    p1 = []
    p2 = []
    for i in range(len(lst)):
        if i % 2 == 0:
            p1.append(lst[i])
            ans = bg(1)
            if ans != 0:
                break
        else:
            p2.append(lst[i])
            ans = bg(2)
            if ans != 0:
                break
    print(f'#{tc} {ans}')