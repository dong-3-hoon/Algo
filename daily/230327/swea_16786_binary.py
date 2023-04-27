T = int(input())

for tc in range(1, T + 1):
    n, hex_num = input().split()
    n = int(n)
    print(f"#{tc}", end=" ")
    for i in range(n):
        num = int(hex_num[i], 16)
        for j in range(3, -1, -1):
            if num & (2 ** j) == 0:
                print("0", end="")
            else:
                print("1", end="")
    print()