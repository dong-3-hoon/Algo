T = int(input())

for tc in range(1, T + 1):
    # 층, 호, c번째 손님
    a, b, c = map(int, input().split())
    arr = [['0'] * b for _ in range(a)]
    stk = [[0]*b for _ in range(a)]
    # 아래에서 위로, 앞에서부터 뒤로 방 번호를 배정
    for i in range(a, 0, -1):
        for j in range(1, b+1):
            arr[a-i][j-1] = str(i)
            # 10 이하일때는 101, 201 등 사이에 0 삽입
            if j<10:
                arr[a-i][j-1] += '0'
                arr[a-i][j-1] += str(j)
            else:
                arr[a-i][j-1] += str(j)
    # 전체 방에서 손님이 들어갈 순서 배정
    cnt = 1
    for j in range(b):
        for i in range(a):
            stk[a-i-1][j] = cnt
            cnt += 1
    # 손님 방 번호를 출력
    for i in range(a):
        for j in range(b):
            if stk[i][j] == c:
                print(arr[i][j])