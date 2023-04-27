import sys

sys.stdin = open('newbus.txt')
T = int(input())

for tc in range(1, T+1):
    bus_num = int(input())
    bus_info = []
    max_stop = 0
    # 버스 정보를 리스트로 받음
    for i in range(bus_num):
        A = list(map(int, input().split()))
        bus_info.append(A)
    print(bus_info)
    # 마지막 정류장을 구함
    for i in bus_info:
        if i[2] > max_stop:
            # 여기서 +1을 해주면 9가 들어갈 때 10이 저장 다음 10때는 if문 안으로 안 들어간다.
            max_stop = i[2]
    # print(max_stop)
    all_stop = [0] * (max_stop+1)
    # all_stop = [0] * 1001
    for i in bus_info:
        # 일반 버스
        if i[0] == 1:
            for j in range(i[1], i[2]+1):
                all_stop[j] += 1
        # 급행 버스
        elif i[0] == 2:
            # A가 짝수면 짝수 번호 정류장만 정차
            if i[1] % 2 == 0:
                for j in range(i[1], i[2] + 1):
                    if j % 2 == 0:
                        all_stop[j] += 1
            # A가 홀수면 홀수 번호 정류장만 정차
            else:
                for j in range(i[1], i[2] + 1):
                    if j % 2 == 1:
                        all_stop[j] += 1
        # 광역 버스
        else:
            # A가 짝수면 4배수 정류장에 정차
            if i[1] % 2 == 0:
                for j in range(i[1], i[2] + 1):
                    if j % 4 == 0:
                        all_stop[j] += 1
            # A가 홀수면 3의 배수이면서 10의 배수 x시 정차
            else:
                for j in range(i[1], i[2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        all_stop[j] += 1
    busy_stop = 0
    # print(all_stop)
    for i in all_stop:
        if i > busy_stop:
            busy_stop = i
    print(f'#{tc} {busy_stop}')