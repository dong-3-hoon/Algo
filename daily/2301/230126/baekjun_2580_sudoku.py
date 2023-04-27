def searchnum(mid_lst):
    for i in range(1,10):
        if i not in mid_lst:
            return i

#가로를 탐색해서 0의 갯수가 1이면 없는 숫자를 채움
def width_search(lst):
    for lst_line in lst:
        zerocnt=lst_line.count(0)
        if zerocnt==1:
            for lst_line_num in range(1, 10):
                if lst_line_num not in lst_line:
                    lst_line[lst_line.index(0)]=lst_line_num
    return lst

#세로를 탐색해서 0의 갯수가 1이면 없는 숫자를 채움
def length_search(lst):
    rot_lst=list(map(list, zip(*lst)))
    for lst_line in rot_lst:
        zerocnt=lst_line.count(0)
        if zerocnt==1:
            for lst_line_num in range(1, 10):
                if lst_line_num not in lst_line:
                    lst_line[lst_line.index(0)]=lst_line_num
    lst=list(map(list, zip(*rot_lst)))
    return lst

#box를 탐색해서 0의 갯수가 1이면 0을 1-9에서 없는 수로 바꿔준다.
def box_search(lst):
    #이중포문으로 00 03 06 30 33 36 60 63 66 탐색해서 하기.
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0
    for i in range(3):
        for j in range(3):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num

    mid_lst, new_num, cnti, cntj=[], 0, 0, 0
    for i in range(3):
        for j in range(3,6):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num

    mid_lst, new_num, cnti, cntj=[], 0, 0, 0
    for i in range(3):
        for j in range(6,9):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0
    
    for i in range(3,6):
        for j in range(3):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0

    for i in range(3,6):
        for j in range(3,6):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0

    for i in range(3,6):
        for j in range(6,9):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0

    for i in range(6,9):
        for j in range(3):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    mid_lst, new_num, cnti, cntj=[], 0, 0, 0

    for i in range(6,9):
        for j in range(3,6):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num

    mid_lst, new_num, cnti, cntj=[], 0, 0, 0
    for i in range(6,9):
        for j in range(6,9):
            mid_lst.append(lst[i][j])
            if lst[i][j]==0:
                cnti, cntj=i, j
    if mid_lst.count(0)==1:
        new_num=searchnum(mid_lst)
        lst[cnti][cntj]=new_num
    return lst

lst, cnt, totalzero=[], 0, 0
for i in range(9):
    a=list(map(int, input().split()))
    lst.append(a)
#0의 갯수 탐색
while True:
    cnt+=1
    for i in lst:
        for j in i:
            if j==0:
                totalzero+=1
    #0의 갯수가 0이면 break
    if totalzero==0:
        for i in range(9):
            for j in range(9):
                print(lst[i][j], end=' ')
            print()
        break
    #아니면 함수를 호출해서 0의 갯수를 줄인다.
    else:
        lst=width_search(lst)
        lst=length_search(lst)
        lst=box_search(lst)
        totalzero=0
