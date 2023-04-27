import sys
sys.stdin = open("daily/230328/1244.txt")


def dfs(idx, cnt):
    global answer
    # 종료 조건
    if cnt == int(target):
        answer = max(int("".join(nums)), answer)
        return
    
    for now in range(idx, n):
        for max_idx in range(now + 1, n):
            if nums[now] <= nums[max_idx]:
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
                dfs(now, cnt + 1)
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
    # 교환 횟수가 남았을 때
    if not answer and cnt < int(target):
        rotate = (int(target) - cnt) % 2
        if rotate:
            # 마지막 2개를 교환
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, int(target))


for test in range(1, int(input()) + 1):
    nums, target = input().split()
    n = len(nums)
    nums = list(nums)
    answer = 0
    dfs(0, 0)
    print(f'#{test} {answer}')