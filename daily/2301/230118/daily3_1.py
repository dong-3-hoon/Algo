fruit=input().split(',')
stk=''
newfruit=[]
for i in fruit:
    if 'rotten' in i:
        for j in range(6,len(i)):
            stk+=i[j]
        newfruit.append(stk)
        stk=''
    else:
        newfruit.append(i)
print(newfruit)