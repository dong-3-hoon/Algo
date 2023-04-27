import random
while True:
    cumputer=random.randrange(1,4)
    #cumputer=random.choice(["가위", "바위", "보"])
    user=input('가위, 바위, 보 중 하나 입력하시요(종료: -1): ')
    #가위=1, 바위=2, 보=3
    if user=='-1':
        break
    if cumputer==1:#가위
        if user=='가위':
            print('비김')
        elif user=='바위':
            print('내가 이김')
        elif user=='보':
            print('내가 짐')
        else:
            print('가위, 바위, 보 중 하나를 입력하시오')
    elif cumputer==2:#바위
        if user=='가위':
            print('내가 짐')
        elif user=='바위':
            print('비김')
        elif user=='보':
            print('내가 짐')
        else:
            print('가위, 바위, 보 중 하나를 입력하시오')
    else:#보
        if user=='가위':
            print('내가 이김')
        elif user=='바위':
            print('내가 짐')
        elif user=='보':
            print('내가 짐')
        else:
            print('가위, 바위, 보 중 하나를 입력하시오')

