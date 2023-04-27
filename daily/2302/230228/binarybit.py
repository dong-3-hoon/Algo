pat = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}

h1 = "0DEC"
h2 = "0269FAC9A0"


def find_pattern(n):
    # n은 16진수로 되어있는 문자열
    # 이진수로 바꾸면 길이 4배 증가
    l = len(n) * 4
    x = int(n, 16)
    print(l)
    # 이진수로 바꾸기
    bin = ""
    for i in range(l - 1, -1, -1):
        # i번째 비트가 1인지 아닌지
        bin += "1" if x & (1 << i) else "0"
    # 뒤에서부터 검사해서 1을 만나면 암호 해독
    # 암호 해독 후 결과
    res = []
    bin = list(bin)
    print(bin)
    for i in range(l - 1, 5, -1):
        # 1을 만난 순간 6개씩 잘라서 검사
        if bin[i] == "0":
            continue
        # 6개씩 슬라이싱
        code = bin[i : i - 6 : -1]
        # 뒤집기
        code = code[::-1]
        # 문자열로 만들기
        code_str = "".join(code)
        # 사전에서 찾기
        dec = pat.get(code_str)
        # 사전안에 패턴이 있는 경우
        print(dec, code_str)
        if dec != None:
            res.append(dec)
            # 이미 탐색한 앞의 5칸을 0으로 바꿔줌
            for j in range(i, i - 6, -1):
                bin[j] = "0"
    # 코드 출력
    print(res[::-1])


find_pattern(h1)
find_pattern(h2)
