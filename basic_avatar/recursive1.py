def function1(num):
    print("now", num)

    # 1. 반드시 종료 조건을 정한다.
    if num == 0:
        return
    # 2. 종료조건이 아닌 경우에 재귀 호출
    # 언젠가는 종료조건을 만족하도록 변경 해줘야한다.
    else:
        function1(num - 1)

    print("back", num)


function1(5)


def fact(n):
    # 1. 종료 조건
    if n == 1:
        return 1
    # 2. 재귀 호출
    else:
        return n * fact(n - 1)


print(fact(5))

n = 20
memo = [0] * 20
memo[1] = 1


def fibo(n):
    # n 번째 항을 계산한적이 없고, n이 2 이상이라면
    # n 번째 항을 계산 해야된다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n - 1) + fibo(n - 2)
        print(memo[n])

    # 계산한적이 있으면 memo[n] 값을 그대로 사용하면 된다.
    return memo[n]


print(fibo(7))
