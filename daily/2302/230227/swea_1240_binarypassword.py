import sys

from pprint import pprint

sys.stdin = open("daily/230227/1240.txt")


# 비밀번호 형식이 맞는지 검사하는 함수
def vali(st):
    even = 0
    odd = 0
    ans = 0
    for i in range(len(st)):
        if i % 2 == 0:
            even += int(st[i])
        else:
            odd += int(st[i])
    # 짝수 홀수를 나눠서 10으로 나누어 떨어지면 True 리턴
    if (even + odd * 3) % 10 == 0:
        return True
    else:
        return False


# 문자열을 각 숫자로 변환하는 함수
def trans(st):
    print(st)
    if st[::-1] == "0001101":
        return "0"
    elif st[::-1] == "0011001":
        return "1"
    elif st[::-1] == "0010011":
        return "2"
    elif st[::-1] == "0111101":
        return "3"
    elif st[::-1] == "0100011":
        return "4"
    elif st[::-1] == "0110001":
        return "5"
    elif st[::-1] == "0101111":
        return "6"
    elif st[::-1] == "0111011":
        return "7"
    elif st[::-1] == "0110111":
        return "8"
    elif st[::-1] == "0001011":
        return "9"


# 문자열을 56번째부터 0번째 까지 구함
def deco(i, j):
    st = ""
    ans = ""
    for x in range(56):
        st += arr[i][j - x]
        # 56개를 모두 찾았으면 숫자로 변환한 것을 리턴
        if x == 55:
            ans += trans(st)
            return ans
        # 길이가 7이 될 때마다 숫자로 변환하고 다시 초기화
        if len(st) == 7:
            ans += trans(st)
            st = ""


T = int(input())
for tc in range(1, T + 1):
    arr = []
    answer = 0
    st = ""
    A, B = map(int, input().split())
    for i in range(A):
        lst = list(input())
        arr.append(lst)
    # 리스트를 거꾸로 돌면서 1을 찾고 찾은 후 함수 호출
    for i in range(A):
        for j in range(B - 1, -1, -1):
            if arr[i][j] == "1":
                st = deco(i, j)
                if len(st) != 0:
                    break
        # 문자열이 0 이아니면 반복문을 탈출
        if len(st) != 0:
            break
    k = vali(st)
    # 비밀번호 형식이 맞다면 값을 출력
    if k == True:
        for i in range(len(st)):
            answer += int(st[i])
        print(f"#{tc} {answer}")
    else:
        print(f"#{tc} {answer}")
