def compare(lst):
    return max(lst)
tc = 1
while True:
    num = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for i in range(len(height)):
        comp = 0
        lst = []
        if i == 0:  # 앞쪽 2개만 판단
            if height[i] > height[i+1] and height[i] > height[i+2]:
                if height[i] > height[i + 1] and height[i] > height[i + 2]:
                    lst.append(height[i + 1])
                    lst.append(height[i + 2])
                    comp = compare(lst)
                    answer += height[i] - comp
        if i == 1:  # 앞쪽 2개, 뒷쪽 1개만 판단
            if height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i+2]:
                lst.append(height[i-1])
                lst.append(height[i+1])
                lst.append(height[i+2])
                comp = compare(lst)
                answer += height[i] - comp
        if i == 98:  # 뒷쪽 2개, 앞쪽 1개만 판단
            if height[i] > height[i-2] and height[i] > height[i-1] and height[i] > height[i+1]:
                lst.append(height[i - 2])
                lst.append(height[i - 1])
                lst.append(height[i + 1])
                comp = compare(lst)
                answer += height[i] - comp
        if i == 99:  # 뒷쪽 2개만 판단
            if height[i] > height[i-1] and height[i] > height[i-2]:
                lst.append(height[i-1])
                lst.append(height[i-2])
                comp = compare(lst)
                answer += height[i] - comp
        else:  # 앞쪽 2개, 뒷쪽 2개 판단
            if height[i] > height[i - 2] and height[i] > height[i - 1] and height[i] > height[i + 1] and height[i] > height[i+2]:
                lst.append(height[i - 2])
                lst.append(height[i - 1])
                lst.append(height[i + 1])
                lst.append(height[i + 2])
                comp = compare(lst)
                answer += height[i] - comp
    print(f"#{tc} {answer}")
    tc += 1
    if tc == 11:
        break