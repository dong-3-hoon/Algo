numbers = [1, 2, 3, 4, 5]
n = 5


# i 번째 원소의 자리를 바꿔가며 순열 생성
# 자리를 바꿀 수 있는 경우의 수
def perm1(i):
    global cnt1
    # 종료 조건
    if i == n:
        cnt1 += 1
        print(numbers)
        return
    # 재귀 호출
    # 현재 위치 i 에서 다른 위치 j에 있는 숫자와 한번씩 다 바꿔보기
    # 이전에 i, j <> j, i 처럼 바꾼것은 중복 처리
    # 위치를 바꾸지 않고 진행 가능 i == j는 위치를 바꾸지 않고 다음 원소의 자리를 바꾸러 이동
    for j in range(i, n):
        # i <-> j 후 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 다음 i+1 번째 원소의 자리를 바꾸러 간다
        perm1(i + 1)
        # i  번째와 j 번째 위치를 되돌려 놓고 다음 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]


# i 번째의 자리를 누구로 할 것인가 선택하는 방법
# i 번째 자리가 누군지 기억해야 하므로 배열 필요


def perm2(i, selected):
    global cnt2
    if i == n:
        cnt2 += 1
        print(selected)
    # 현재 위치 i에 누구를 놓을 것인가
    for j in range(n):
        # j 번째 원소를 놓은 적이 없다면 j번째 원소를 i위치에 놓기
        if numbers[j] not in selected:
            # i 위치는 j 번째 원소가 선택되었다.
            selected[i] = numbers[j]
            # i 위치의 주인을 정했으니 i + 1 번째 위치의 주인을 정하러 감
            perm2(i + 1, selected)
            # i 번째 위치의 j를 선택 취소 하고 다음으로 이동
            selected[i] = 0


cnt1 = 0
perm1(0)
cnt2 = 0
perm2(0, [0] * 5)
print(cnt1, cnt2)
