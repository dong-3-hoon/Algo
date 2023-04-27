# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
density=[]
stk1, stk2=0, 0
saltwater=[]
finaldensity=0
finalsalt=0
finalsaltwater=0
cnt=1
while True:
    iinput=input(f'{cnt}. 소금의 농도와 소금물 양을 입력하시오(끝내고 싶다면 Done를 입력하시오): ')
    cnt+=1
    if iinput=='Done' or cnt>5:
        break
    else:
        stk1, stk2=iinput.split()
        density.append(int(stk1))
        saltwater.append(int(stk2))
salt=[]
for i in range(len(density)):
    salt.append((int(density[i])*int(saltwater[i]))/100)
finalsalt=sum(salt)
finalsaltwater=sum(saltwater)
finaldensity=finalsalt/finalsaltwater*100
print(f'농도: {round(finaldensity, 2)}%, 소금물 양: {finalsaltwater}g')