num=int(input())
cnt=0
length=64
stick=[]
while True:
    if length>num:
        length/=2
    else:
        stick.append(length)
        stick.append(length)
        break
print(length, stick)