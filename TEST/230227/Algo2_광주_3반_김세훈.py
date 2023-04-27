import sys

sys.stdin = open("TEST/230227/algo2_sample_in.txt")
from pprint import pprint


# 현재 별의 갯수를 탐색하는 함수
def find_star(x_start, x_end, y_start, y_end):
    cnt = 0
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            # 범위 내부에서 *일 때 카운트 증가
            if 0 <= i < K and 0 < j <= K and arr[i][j] == "*":
                cnt += 1
    return cnt


def zoom(A, B, K, zoom_cnt):
    global star_cnt, ans
    now_cnt = 0
    nxs = A - K // 2 + zoom_cnt
    nxe = A + K // 2 - zoom_cnt + 1
    nys = B - K // 2 + zoom_cnt
    nye = B + K // 2 - zoom_cnt + 1
    # 초점에서 주어진 범위를 기준으로 별 탐색 함수 호출
    now_cnt = find_star(nxs, nxe, nys, nye)
    # 탐색한 별의 갯수가 전체 별의 갯수와 같으면 줌 횟수를 증가시키고 다시 재귀 호출
    if now_cnt == star_cnt:
        zoom(A, B, K, zoom_cnt + 1)
        ans += 1


T = int(input())
for tc in range(1, T + 1):
    # 배열 크기, 영역 크기, 초점
    N, K, A, B = map(int, input().split())
    arr = []
    ans = 0
    # 전체 별의 갯수
    star_cnt = 0
    # 줌 횟수
    zoom_cnt = 0
    # 배열 생성
    for _ in range(N):
        lst = list(input().split())
        arr.append(lst)
    # 전체 별 갯수 탐지
    star_cnt = find_star(1, K, 1, K)
    # 줌을 하면서 별의 갯수를 탐지
    zoom(A, B, K, zoom_cnt)
    # 0보다 크다면 줌을 했기 때문에 줌 횟수를 출력
    if ans > 0:
        print(f"#{tc} {ans-1}")
    # 0과 같다면 처음부터 모든 별을 다 담을 수 없기 때문에 -1 출력
    else:
        print(f"#{tc} {-1}")
