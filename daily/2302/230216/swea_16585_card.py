import sys

# from pprint import pprint
sys.stdin = open("daily/230216/16585.txt")


def winner(left, right):
    # 가위 보 에서는 가위 리턴
    if left == 1 and right == 3:
        return left
    elif left == 3 and right == 1:
        return right
    # 아니면 큰 수를 리턴
    else:
        if left < right:
            return right
        else:
            return left


# 길이를 받는다
def tor(part, end):
    A, B = [], []
    P = []
    global start
    # 길이가 2인 경우 계산을 한다.
    if len(part) == 3:
        return winner(winner(part[0], part[1]), part[2])
    if len(part) == 2:
        return winner(part[0], part[1])
    else:
        # 전체 길이가 짝수
        if end % 2 == 0:
            # 반은 A조, 나머지는 B조
            for i in range(end // 2):
                A.append(part[i])
            for i in range(end // 2, end):
                B.append(part[i])
            start += 1
            P.append(tor(A, end // 2))
            P.append(tor(B, end // 2))
            start -= 1
        # 전체 길이가 홀수
        else:
            for i in range(end // 2 + 1):
                A.append(part[i])
            for i in range(end // 2 + 1, end):
                B.append(part[i])
            start += 1
            P.append(tor(A, end // 2 + 1))
            P.append(tor(B, end // 2))
            start -= 1
    print(P)


T = int(input())

# 1 = sci, 2 = rock, 3 = paper
for tc in range(1, T + 1):
    start = 0
    end = int(input())
    rnd = end // 2 + 1
    info = [[] for i in range(rnd)]
    info[start] = list(map(int, input().split()))
    print(info[0])
    tor(info[start], end)
