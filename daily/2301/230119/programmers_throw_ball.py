def solution(numbers, k):
    answer = 1
    cnt=0
    if len(numbers)%2==0:
        while True:
            if answer==k:
                return numbers[cnt]
            if cnt>=len(numbers):
                cnt=0
            answer+=1
            cnt+=2
    else:
        while True:
            if answer==k:
                return numbers[cnt-1]
            if cnt>=len(numbers)-1:
                cnt=1
            answer+=1
            cnt+=2
print(solution([1, 2, 3], 3))