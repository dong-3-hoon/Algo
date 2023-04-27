import sys

# from pprint import pprint
sys.stdin = open("daily/230215/1222.txt")


def get_post(infix, n):
    post = ""
    stack = []
    for i in range(n):
        if "0" <= infix[i] <= "9":
            post += infix[i]
        else:
            stack.append(infix[i])
    while stack:
        post += stack.pop()
    return post


def get_result(post):
    stack = []
    for c in post:
        if "0" <= c <= "9":
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()
            if c == "+":
                result = left + right
            stack.append(result)
    return stack.pop()


cnt = 1
while cnt < 11:
    n = int(input())
    string = list(input())
    postfix = get_post(string, n)
    print(f"#{cnt} {get_result(postfix)}")
    cnt += 1
