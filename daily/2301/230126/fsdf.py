def row(x,y,j,num_list):
    print(x, y, j, num_list)
    for k in range(9):
        if j not in num_list[x][k]:
            return True
        else:
            return False

def col(x,y,j,num_list): 
    for kk in range(9):
        if j not in num_list[kk][y]:
            return True
        else:
            return False

def find_zero(num_list):
    zero = []
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if num_list[i][j] == 0:
                zero.append((i,j))

    for j in range(1,10):
        x = zero[j-1][0]
        y = zero[j-1][1]
        print(x, y, j, num_list)
        if row(x,y,j,num_list):
            if col(x,y,j,num_list):
                num_list[x][y] = j

num_list = [list(map(int, input().split())) for _ in range(9)]
find_zero(num_list)