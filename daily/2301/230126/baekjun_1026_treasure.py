leng = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
stk=[]
arrA.sort()
for i in range(leng):
    stk.append(arrA[i]*max(arrB))
    arrB.remove(max(arrB))
print(sum(stk))
#