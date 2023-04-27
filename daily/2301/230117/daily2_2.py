# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

x=input()
lst=[]
lst_result=[]
for i in x:
    lst.append(i)
print(lst)
if lst[0]=='<' and lst[1] == 'p' and lst[2] == '>':
    lst.remove(lst[0])
    lst.remove(lst[0])
    lst.remove(lst[0])
print(lst[-1])
if lst[-1]=='>' and lst[-2] == 'p' and lst[-3] == '/' and lst[-4]=='<':
    lst.remove(lst[-1])
    lst.remove(lst[-1])
    lst.remove(lst[-1])
    lst.remove(lst[-1])

for i in lst:
    print(i, end='')