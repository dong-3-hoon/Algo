import sys

# from pprint import pprint
sys.stdin = open("daily/230215/16530.txt")
icp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 3}
isp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0}


def get_result(postfix):
    stack = []
    for c in postfix:
        if c == ".":
            if len(stack) == 1:
                return stack.pop()
            else:
                return "error"
        if "0" <= c <= "9":
            stack.append(int(c))
        else:
            if len(stack) < 2:
                return "error"
            right = stack.pop()
            left = stack.pop()
            if left == "0":
                return "error"
            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "/":
                result = int(left / right)
            elif c == "*":
                result = left * right
            stack.append(result)
    return stack.pop()


T = int(input())

for tc in range(1, T + 1):
    string = list(input().split())
    n = len(string)
    print(f"#{tc} {get_result(string)}")
