import sys

# from pprint import pprint
sys.stdin = open("daily/230217/4408.txt")

# 시작 복도 번호 ~ 끝 복도 번호: 누적 cnt 표시
# (방 번호 -1) // 2: 복도 번호
# 최대값 찾기
# 모두 0, 모두 mx값, 값이 1개만, 음수 포함, 정렬 x, 경계에만 값
T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    cnt = [0] * 200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        # 복도가 겹치는 횟수만큼 시간이 걸려야 모두 자신의 방으로 돌아갈 수 있다
        for i in range((s - 1) // 2, (e - 1) // 2 + 1):
            cnt[i] += 1
    ans = max(cnt)
    print(f"#{tc} {ans}")
