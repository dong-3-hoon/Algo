def solution(n):
    answer = []
    cnt=2
    stk=n
    while cnt<20:
        if n==cnt:
            answer.append(n)
            return answer
        if stk%cnt==0:
            stk=stk//cnt
            if cnt not in answer:
                answer.append(cnt)
            cnt=2
        else:
            cnt+=1
        if stk==1:
            return answer


solution(12)
solution(7)
solution(420)