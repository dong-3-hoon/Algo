stk=1
sset=set()
while True:
    two_DA=stk*2
    seven_DA=stk*7
    if two_DA<1000:
        sset.add(two_DA)
    if seven_DA<1000:
        sset.add(seven_DA)
    stk+=1
    if two_DA>1000:
        break
print(sum(sset))