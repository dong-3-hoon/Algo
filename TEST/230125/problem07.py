# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    pass
    # 길이가 1이면 원의 넓이 리턴
    if len(numbers)==1:
        return (numbers[0]**2)*3.14
    # 길이가 0이면 0 리턴
    elif len(numbers)==0:
        return 0
    # 길이가 2
    elif len(numbers)==2:
        #나머지가 0인 짝수 일때는 사각형의 넓이 리턴
        if sum(numbers)%2==0:
            return numbers[0]*numbers[1]
        #나머지가 1인 홀수 일때는 삼각형의 넓이 리턴
        else:
            return numbers[0]*numbers[1]/2
    # 길이가 3 이상이면 값들의 합, 평균을 튜플로 리턴
    else:
        answer=()
        answer=sum(numbers), sum(numbers)/len(numbers)
        return answer


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0