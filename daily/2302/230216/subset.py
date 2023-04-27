numbers = [1, 2, 3, 4, 5]

# selected[i] == 1 > 내가 i번째 원소를 부분집합에 포함
# selected[i] == 0 > 내가 i번째 원소를 부분집합에 미포함
selected = [0] * 5

n = len(numbers)

# 합이 x 보다 작은 부분집합만 구해야 한다면?
x = 6


def subset(i, sub_sum):
    # 재귀함수로 부분집합 구하기
    # i 번째 원소를 부분집합에 포함 할지 말지 결정
    # 가지치기
    if sub_sum >= x:
        return
    # 종료 조건
    if i == n:
        # n개의 원소에 대해 선택을 끝냈다. (고르던지 말던지)
        for j in range(n):
            if selected[j]:
                print(numbers[j], end=" ")
        print()
        print("========")
        return
    # 재귀 호출
    # i번째를 선택하고(부분집합에 포함) 다음 i+1 번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1, sub_sum + numbers[i])
    # i 번째를 선택하지 않고(부분집합에 미포함) 다음 i+1번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1, sub_sum)


subset(0, 0)
