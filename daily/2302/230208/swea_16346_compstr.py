import sys
sys.stdin = open('daily/230208/16346.txt')
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for i in range(len(str2)):
        cnt = 0
        for j in range(len(str1)):
            if i+j<len(str2):
                if str2[i+j] == str1[j]:
                    cnt += 1
                if cnt == len(str1):
                    ans = 1
    print(f'#{tc} {ans}')