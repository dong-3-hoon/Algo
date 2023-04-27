mystr=input()
middle=0
if len(mystr)%2==0:
    middle=int(len(mystr)/2)
    print(mystr[middle-1],mystr[middle])
else:
    middle=int(len(mystr)/2-0.5)
    print(mystr[middle])