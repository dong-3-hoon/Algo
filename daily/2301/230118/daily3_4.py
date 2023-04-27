blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
people=dict()

for i in blood_types:
    if i not in people.keys():
        people[i]=1
    else:
        people[i]+=1

print(people)