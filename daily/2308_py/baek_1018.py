x, y = map(int, input().split())
change_cnt = 50*50
white_chess = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

black_chess = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
my_chess=[]
for i in range(x):
    my_chess.append(list(map(str, input())))
for i in range(x-7):
    for j in range(y-7):
        # compare white chess
        cnt = 0
        for k in range(8):
            for l in range(8):
                if white_chess[k][l] != my_chess[i+k][j+l]:
                    cnt += 1
        if cnt<change_cnt:
            change_cnt = cnt

        # compare black chess
        cnt = 0
        for k in range(8):
            for l in range(8):
                if black_chess[k][l] != my_chess[i+k][j+l]:
                    cnt += 1
        if cnt < change_cnt:
            change_cnt = cnt
print(change_cnt)