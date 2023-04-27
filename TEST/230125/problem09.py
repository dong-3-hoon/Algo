answer=[]
# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    pass
    #answer변수를 전역변수로 설정해서 연산값 저장
    global answer
    #반환할 문자열
    star=''
    #몫이 1 이상이면 재귀로 함수 호출
    if number//2>1:
        answer.append(number%2)
        dec_to_bin(number//2)
    #몫이 2 미만이면 answer에 저장된 변수를 문자열에 넣고 리턴
    else:
        answer.append(number%2)
        answer.append(1)
        for i in range(len(answer)-1, -1, -1):
            star+=str(answer[i])
        answer=[]
        return print(star)
'''
def dec_to_bin(number):
    
    if number<2:
        return str(number)
    else:
        return dec_to_bin(number // 2) + str(number % 2)
'''
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
