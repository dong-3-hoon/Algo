# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 
def de_identify(number):
    #빈 문자열 생성
    strr=''
    for i in range(len(number)):
        #'-' 가 아닌 문자 중
        if number[i] != '-':
            #이후에는 *삽입
            if i>5:
                strr+='*'
            #0-5까지는 숫자를 삽입
            else:
                strr+=str(number[i])
    print(strr)
    print('hi')
        


de_identify('970103-1234567')
de_identify('8611232345678')
