cnt = 0
resi_list = []
while True:
    resi_list.append(input())
    cnt += 1
    if cnt>2:
        break

third = 0
strr = ''
color_cnt = {'black': 0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
color_x = {'black':1, 'brown':10, 'red':100, 'orange':1000, 'yellow':10000, 
         'green':100000, 'blue':1000000, 'violet':10000000, 'grey':100000000, 'white':1000000000}

for i in range(len(resi_list)):
    if i==2:
        third = color_x[resi_list[i]]
    elif i==1:
        strr += str(color_cnt[resi_list[i]])
    else:
        strr += str(color_cnt[resi_list[i]])

print(int(strr)*third)
