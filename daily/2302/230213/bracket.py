import sys

sys.stdin = open("daily/230213/rhkfghrjatk.txt")
# from pprint import pprint
T = int(input())

for tc in range(1, T + 1):
    row = input()
    stack = []
    answer = 1  # 1이면 맞음, 0이면 틀림
    for c in row:
        # 열린 괄호가 나오면 스택에 push
        if c == "(":
            stack.append(c)
        # 닫힌 괄호가 나오면 스택에서 pop해서 나온 괄호와 짝이 일치하는지 검사
        # 스택에서 pop해서 나온 괄호와 짝이 일치하는지 검사
        if c == ")":
            if len(stack) == 0:
                answer = 0
                break
            b = stack.pop()
            if not (b == "(" and c == ")"):
                answer = 0
                break
    # 반복이 다 끝나고 나서 남은 괄호가 스택에 있는지 검사
    if len(stack) > 0:
        answer = 0
    print(f"#{tc} {answer}")
