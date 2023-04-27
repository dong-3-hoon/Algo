bottle, carry = map(int, input().split())
bin_bot=bin(bottle)
lst=[]
cnt=0
if bottle == carry:
    print(0)
    quit()
if bottle<carry:
    print(-1)
    quit()
a='0b'
for i in range(carry+2, len(bin_bot)):
    lst.append(bin_bot[i])
for i in lst:
    a+=i
b=int(a, 2)
if b==0:
    print(0)
    quit()
c=2**(len(lst))
print(c-b)