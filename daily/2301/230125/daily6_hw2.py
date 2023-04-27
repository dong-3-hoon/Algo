grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
cnt=0
#문자열의 숫자값 중 큰 값을 저장
for i in grain_lst:
    if i[1]>cnt:
        cnt=i[1]
#가장 큰 값에서의 이름을 출력
for i in grain_lst:
    if i[1]==cnt:
        print(i[0])