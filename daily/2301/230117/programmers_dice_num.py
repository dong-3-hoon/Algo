def solution(box, n):
    answer = 1
    stk=[]
    for i in box:
        stk.append(i//n)
    for i in stk:
        answer*=i
    return answer