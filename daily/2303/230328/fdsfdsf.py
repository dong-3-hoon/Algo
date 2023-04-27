import sys
sys.stdin = open("daily/230328/1244.txt")

def dfs(n, level, S):
    if n == level : #해당 문자를 level번 순열 돌렸을 때 나올 수 있는 최고값 메모
        memo[n] = max(memo[n], int(''.join(S)))
        return
    
    # 순열 돌리기
    for i in range(len(N)):
        for j in range(i+1, len(N)):
            S[i], S[j] = S[j], S[i]
            dfs(n+1, level, S)
            S[i], S[j] = S[j], S[i]

T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    N = list(N)
    M = int(M)
    memo = [0] * (M+1)
    idx = 0
    for i in range(M+1):
        dfs(0, i, N) # 메모이제이션 사용을 위해 각 교환횟수별 최고값 담아두기
        idx = i

        #반복이 나타나는 경우 2가지 :
        # 1. 현재값과 이전값의 최고값이 같은경우 A, B
        # 2. 현재값과 전전 값이 같아서 A, B, A, B가 나오는 경우

        if i >= 1 and memo[i] == memo[i-1] :  # A, A인 경우
            break
        elif i >= 2 and memo[i] == memo[i-2] : #A, B, A 인경우
            break

    # 끝난 idx가 홀수일 경우
    if idx % 2 :
        # 찾는 번호도 홀수일경우
        if M % 2 :
            print(f"#{tc}", memo[idx])
        else : #찾는 번호는 짝수일경우
            print(f"#{tc}",memo[idx-1])

    # 끝난 idx가 짝수일경우
    else :
        if M % 2 : #찾는 번호가 홀수일경우
            print(f"#{tc}",memo[idx-1])
        else : #찾는 번호도 짝수일경우
            print(f"#{tc}",memo[idx])