#길이, 수식 인풋받음
N = int(input())
expression = input()
answer = -2 ** 31

#만약 1이면 max값을 출력함 
if N == 1:
    print(max(answer, int(expression)))
    exit()
 
symbol = ["+", "-", "*"]
 #parenthesis=괄호
 
def add_parenthesis(index, expression_list):
    global answer
    #시행 횟수==길이면
    if index == N:
        #enumerate 함수: 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 객체를 리턴
        for i, j in enumerate(expression_list):#i, j의 같은 순서값을 비교
            if len(j) == 3:#만약 lenj가 3이면 계산을 해서 리스트에 추가
                expression_list[i] = str(eval(j))
        #계산
        result = expression_list[0]
        #홀수(숫자)들만 계산
        for _ in range(1, len(expression_list), 2):
            #문자마다 다른 계산 수행(eval함수 참조)
            result = eval(str(result)+expression_list[_]+expression_list[_+1])
 
        if answer < result:
            answer = result
        return
    #계산이 끝나면 바로 앞의 문자를 불러와서 len3의 원소를 만들고 재귀로 빠져나와서 다시 원소들을 추가
    #일반적 경우
    #exlist에 두번째 자리를 추가하고
    expression_list.append(expression[index])
    #인덱스를 추가시킨 후 재호출
    add_parenthesis(index + 1, expression_list)
    #식의 맨 마지막을 통합
    del expression_list[-1]
    #만약 맨 마지막 원소의 str길이가 3이면 실시?
    #맨 마지막에 괄호를 씌울 수 있으면 씌움
    if expression_list[-1] in symbol and index + 3 <= N:
        expression_list.append(expression[index:index+3])
        add_parenthesis(index + 3, expression_list)
        del expression_list[-1]
 
#1과 수식의 첫 자리를 가지고 함수를 호출한다.
add_parenthesis(1, [expression[0]])

print(answer)