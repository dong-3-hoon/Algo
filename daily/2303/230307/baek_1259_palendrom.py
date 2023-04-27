lst = []
while True:
    a = input()
    if a != "0":
        lst.append(a)
    else:
        break
for i in lst:
    if i == i[::-1]:
        print("yes")
    else:
        print("no")
