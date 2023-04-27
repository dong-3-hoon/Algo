s = input('숫자를 입력해주세요 : ')
cnt=0
deci=10
ss=[]
per=0#나머지
share=0#몫
for i in s:#인풋된 문자열을 활용해 자릿수를 탐색
    cnt+=1#자릿수
num=int(s)#인풋을 숫자로 변환
for i in range(cnt, 1, -1):
    share=num//(deci**(i-1)) #큰 자릿수부터 몫을 share에 할당
    num=num%(deci**(i-1))#나머지는 새로운 num으로 저장
    ss.append(share)#share을 list에 추가
ss.append(num)
print(sum(ss))