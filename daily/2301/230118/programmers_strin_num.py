
def solution(my_string):
    my_string+='a' #마지막 숫자가 있는 것을 방지하기 위해 문자를 추가
    answer = 0#숫자만 더한 수
    truecnt=[]#숫자의 위치를 저장하는 리스트
    kkk=''#숫자를 문자열 형태로 저장하는 변수
    real=[]#kkk를 저장해서 int로 추출
    for i in my_string:
        if i.isdigit()==True:
            truecnt.append(i)
        else:
            truecnt.append(-1)
    for i in range(len(truecnt)):
        if int(truecnt[i])>-1:
            kkk+=str(truecnt[i])
            if truecnt[i+1]==-1:
                real.append(kkk)
                kkk=''
    for i in real:
        answer+=int(i)
    return answer
    
print(solution("aAb1B2cC34oOp"))
