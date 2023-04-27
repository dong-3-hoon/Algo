import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    # 상자 탑의 수
    n = int(input())

    # 상자 탑 높이 정보
    box = list(map(int, input().split()))

    # 최댓값 => 초기값 정할 때 적당히 작은 값
    # 최솟값 => 적당히 큰 값
    answer = 0
    # 반복문을 돌면서 현재 위치의 높이에서 제일 위에 있는 상자의 낙차 중에 가장 큰 값을 구하면 된다.
    for i in range(n):
        ans = 0
        # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물이(상자가 없다고 했을 때 떨어질 수 있는 최대 낙차를 구해라
        # 또 반복문을 돌면서 현재 내 위치 기준 오른쪽에 있는 장애물(상자) 의 수 구하기
        # 최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 = 오른쪽 상자 수
        # 최대 낙차 중 최댓값을 갱신
        for j in range(i+1, n):
            if box[i] != box[j] and box[i] > box[j]:
                ans += 1
        if ans > answer:
            answer = ans
    print(f'#{tc} {answer}')