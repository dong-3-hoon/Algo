import sys

# from pprint import pprint
sys.stdin = open("daily/230220/16639.txt")


T = int(input())

for tc in range(1, T + 1):
    # n은 오븐 크기, m 은 피자 개수
    n, m = map(int, input().split())

    # 우리가 구워야할 피자들의 치즈 정보
    pizza_list = list(map(int, input().split()))

    # 다음에 꺼내올 피자의 번호
    next_i = 0

    # 오븐
    oven = [0] * 1000
    o_front = o_rear = -1

    # 오븐 크기만큼 차례대로 피자를 넣기
    for i in range(n):
        # 피자를 넣기 (나중에 꺼낼때를 위해서 피자 번호도 같이 넣기)
        # 오븐 끝
        o_rear += 1
        oven[o_rear] = [i, pizza_list[i]]
        # 오븐 크기가 3이니 다음 인덱스는 3일 것임
        next_i += 1

    # 오븐에 남아있는 피자 개수??
    remain = n
    # 마지막에 꺼낸 피자의 번호
    last_index = -1

    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 꺼내서
        o_front += 1
        i, pizza = oven[o_front]

        # 치즈를 녹이고  c // 2
        pizza //= 2

        # 치즈가 0이 안되었다. => 다시 오븐에 넣기
        if pizza != 0:
            o_rear += 1
            oven[o_rear] = [i, pizza]
        # 치즈가 0이 되었다
        else:
            # 현재 오븐의 자리에 남은 피자 하나꺼내서 넣기
            if next_i < m:
                o_rear += 1
                oven[o_rear] = [next_i, pizza_list[next_i]]
                # 하나 꺼냈으니까 다음 피자 위치 바꾸기
                next_i += 1
            # 넣을 피자가 없다.
            else:
                # 넣을 피자가 없을 때마다 리메인 감소
                remain -= 1
                if remain == 0:
                    # 오븐에 남은 피자도 없는 상황이 온다.
                    # 현재 피자의 번호가 답이 된다.
                    # 반복 종료
                    last_index = i
                    break

    print(f"#{tc} {last_index + 1}")
