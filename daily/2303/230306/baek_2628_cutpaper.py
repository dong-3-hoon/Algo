A, B = map(int, input().split())

num = int(input())
max_x = 0
max_y = 0
hori = [0]
prac = [0]
ans = []
lst = [list(map(int, input().split())) for i in range(num)]

for i in range(num):
    if lst[i][0] == 0:
        hori.append(lst[i][1])
    if lst[i][0] == 1:
        prac.append(lst[i][1])
hori.sort()
prac.sort()
for i in range(len(hori)):
    for j in range(len(prac)):
        # 리스트에서 구한 각 수 를 범위로 cnt해서 가장 큰 값을 리턴
        if 0 <= i + 1 < len(hori) and 0 <= j + 1 < len(prac):
            cnt = 0
            for x in range(hori[i]):
                for y in range(prac[j]):
                    cnt += 1
            ans.append(cnt)
print(ans)
