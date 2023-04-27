import sys

sys.stdin = open('input.txt')

tc = 1
while True:
    num = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for i in range(len(height)):
        lst = []
        max_ = 0
        if i == 0 or i == 1 or i == num-1 or i == num-2:
            continue
        else:  # 앞쪽 2개, 뒷쪽 2개 판단
            if height[i] > height[i - 2] and height[i] > height[i - 1]:
                if height[i] > height[i + 1] and height[i] > height[i+2]:
                    for j in [height[i-1], height[i-2], height[i+1], height[i+2]]:
                        if j > max_:
                            max_ = j
                        answer += max_
    print(f"#{tc} {answer}")
    tc += 1
    if tc == 11:
        break
"""import sys

sys.stdin = open('input.txt')

tc = 1
while True:
    num = int(input())
    height = list(map(int, input().split()))
    answer = 0
    comp = 0
    for i in range(2, len(height)-2):
        if height[i] > height[i - 2] and height[i] > height[i - 1]:
            if height[i] > height[i + 1] and height[i] > height[i+2]:
                comp = max(height[i-1], height[i-2], height[i+1], height[i+2])
                answer += (height[i] - comp)
    comp = 0
    print(f"#{tc} {answer}")
    tc += 1
    if tc == 11:
        break"""