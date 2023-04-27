str_lst = list(input('문자열을 입력하세요. : ').split())
result=[]
for i in str_lst:
    result.append(i.upper())
if result[0][-1] == result[1][0]:
    if result[1][-1] == result[2][0]:
        print('Pass')
    else:
        print('Fail')
else:
    print('Fail')