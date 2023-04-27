import sys

sys.stdin = open('16312.txt')
def binary_search(n, key):
    start = 1
    end = n
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2
        #print(start, end, mid)
        if mid == key:
            return cnt
        elif mid>key:
            end = mid
        else:
            start = mid
    return 999

T = int(input())

for tc in range(1, T+1):
    end, A_right, B_right = map(int, input().split())

    A_cnt = binary_search(end, A_right)

    B_cnt = binary_search(end, B_right)
    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif B_cnt < A_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')