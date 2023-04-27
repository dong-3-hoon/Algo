# fn_d(91) 
# 출력 예시 
# 101

def fn_d(num):#num의 gene를 구하는 코드
    answer=0
    right=0
    for k in range(1, num+1):#1부터 자기 자신까지 
        answer=k
        for i in str(k): #자기를 나눈 값+자기 자신
            answer+=int(i)
            #generation이 존재하면 right를 1로 대입
        if answer==num:
            right=1
            #존재하지 않는다면 right를 0으로
    return right
        
#right이 1이면 num이 gene를 가지고 있음, 0이면 gene가 없음

def is_selfnumber(m):#m이 selfnumber 즉 제너레이션을 가지고 있는지 없는지 판별하는 코드
        right=fn_d(m)
        if right==1:
            print('self number가 아닙니다')
        else:
            print('self number입니다')

# is_selfnumber(1)
# is_selfnumber(2)
# is_selfnumber(3)
# is_selfnumber(4)
# is_selfnumber(5)
# is_selfnumber(6)
# is_selfnumber(20)
# is_selfnumber(31)
# is_selfnumber(32)
# is_selfnumber(101)

