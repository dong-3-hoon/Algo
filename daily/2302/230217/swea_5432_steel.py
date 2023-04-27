import sys

# from pprint import pprint
sys.stdin = open("daily/230217/5432.txt")

# 쌓여있는 막대기 수 cnt
# 앞을 체크(index 활용)

T = int(input())
for tc in range(1, T + 1):
    stack = []
    cnt = 0
    ans = 0
    st = input()
    for i in range(len(st)):
        if st[i] == "(":
            cnt += 1
        # 레이저 or 막대기
        else:
            # 레이저
            if st[i - 1] == "(":
                cnt -= 1
                ans += cnt
            # 막대기
            else:
                cnt -= 1
                ans += 1
    print(f"#{tc} {ans}")
