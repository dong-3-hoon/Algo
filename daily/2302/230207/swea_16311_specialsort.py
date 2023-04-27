import sys

sys.stdin = open('sample_input.txt')
def selection_sort(arr, n):
    #맨 앞자리부터 자리의 주인을 정해준다. 큰숫자부터 차례대로
    for i in range(n -1):
        max_idx = i
        # i 의 뒤부터 비교를 시작하면서 최대값을 찾는다
        for j in range(i+1, n):
            #제일 큰 숫자의 인덱스를 찾기
            if arr[max_idx] > arr[j]:
                max_idx = j
        #반복을 다 돌았으면 제일 작은숫자를 현자 자리 i로 이동
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
T = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))
    n=len(lst)
    ans = []
    selection_sort(lst, n)
    for i in range(10):
        if i % 2 ==0:#짝수일때는 큰 수부터 출력
            ans.append(lst[-1-i//2])
        else:#홀수일때는 작은 수부터 출력
            ans.append(lst[i//2])
    print(f'#{tc}', *ans)