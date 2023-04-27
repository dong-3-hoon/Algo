import sys

from pprint import pprint

sys.stdin = open("daily/230228/1242.txt")


# 문자열을 각 숫자로 변환하는 함수
def trans(st, kkk):
    hihi = ""
    for i in range(len(st)):
        st[i] = st[i] // kkk
    for i in st:
        hihi += str(i)
    if hihi == "3211":
        return "0"
    elif hihi == "2221":
        return "1"
    elif hihi == "2122":
        return "2"
    elif hihi == "1411":
        return "3"
    elif hihi == "1132":
        return "4"
    elif hihi == "1231":
        return "5"
    elif hihi == "1114":
        return "6"
    elif hihi == "1312":
        return "7"
    elif hihi == "1213":
        return "8"
    elif hihi == "3112":
        return "9"
    else:
        return "X"


# 암호 코드 압축
def vandi(st):
    lent = len(st)
    stk = []
    cnt = 1
    ans = ""
    # 7의 배수일때만 cnt 스택을 구하고 아니면 구하지 않는다.
    if lent % 7 == 0:
        kkk = lent // 7 // 8
        for i in range(lent):
            if i == 0:
                continue
            if st[i] == st[i - 1]:
                cnt += 1
            else:
                stk.append(cnt)
                cnt = 1
            if len(stk) == 4:
                ans += str(trans(stk, kkk))
                stk = []
        if len(stk) == 3:
            stk.append(1)
            ans += str(trans(stk, kkk))
    if ans:
        return ans
    else:
        return "X"


# 16진수를 2진수로 변경
def hetobi(n):
    l = len(n) * 4
    x = int(n, 16)
    bin = ""
    for i in range(l - 1, -1, -1):
        # i번째 비트가 1인지 아닌지
        bin += "1" if x & (1 << i) else "0"
    # 뒤에서부터 검사해서 1을 만나면 암호 해독
    # 암호 해독 후 결과
    return bin


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


# 의미있는 문자열만 뽑아서 리턴
def deco(i, j):
    st = ""
    ans = ""
    while arr[i][j] != "0":
        st += str(arr[i][j])
        j -= 1
    return st


T = int(input())
for tc in range(1, T + 1):
    arr = []
    pass_code = []
    answer = 0
    st = ""
    bin = ""
    A, B = map(int, input().split())
    for i in range(A):
        lst = list(input())
        arr.append(lst)
    # 리스트를 거꾸로 돌면서 0이 아닌 값을 찾은 후 함수 호출
    for i in range(A):
        for j in range(B - 1, -1, -1):
            if arr[i][j] != "0":
                st = deco(i, j)
                # 코드와 동일값이 입력되면 0으로 만들어줌
                if st[::-1] in pass_code:
                    for k in range(j, j - len(st), -1):
                        arr[i][k] = "0"
                else:
                    # 코드 리스트에 없는 값이라면 리스트에 추가 후 0으로
                    pass_code.append(st[::-1])
                    for k in range(j, j - len(st), -1):
                        arr[i][k] = "0"
    for i in pass_code:
        st = hetobi(i)
        k = vandi(st)
        print(k)
        if "X" not in k:
            p = vali(k)
            if p == True:
                for i in range(len(st)):
                    answer += int(st[i])
                print(f"#{tc} {answer}")
            else:
                print(f"#{tc} {answer}")
    else:
        print(f"#{tc} {answer}")
    # k = vali(st)
    # # 비밀번호 형식이 맞다면 값을 출력
    # if k == True:
    #     for i in range(len(st)):
    #         answer += int(st[i])
    #     print(f"#{tc} {answer}")
    # else:
    #     print(f"#{tc} {answer}")
