# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    password=''
    # 여기에 코드를 작성하여 함수를 완성합니다.
    for i in word:
        #대문자인 경우
        if i.isupper()==True:
            #Z범위 밖으로 나가면
            if ord(i)+n>90:
                #최초 숫자+n-최대숫자로 돌려줌
                password+=chr(65+ord(i)+n-90-1)
            else:
                password+=chr(ord(i)+n)
        #소문자인 경우
        else:
            #z범위 밖으로 나가면
            if ord(i)+n>122:
                #최초 숫자+n-최대숫자로 돌려줌
                password+=chr(97+ord(i)+n-122-1)
            else:
                password+=chr(ord(i)+n)
    return password
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
