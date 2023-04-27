T = int(input())

age=[]
name=[]
for i in range(T):
    A, B = input().split()
    age.append(int(A))
    name.append(B)

for i in range(max(age)+1):
    for j in range(T):
        if i == age[j]:
            print(age[j], name[j])