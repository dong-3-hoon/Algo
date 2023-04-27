import copy
def combi(mynum):#백트래킹으로 중복 조합을 구함
#num1 개 중 mynum개수만큼 뽑은 조합의 리스트를 모두 구함
    if len(mylst) == mynum:#여기서 중복 조합 제거
        if sorted(mylst) not in retlst:
            retlst.append(sorted(mylst))
        return
    for i in range(len(lst)):
        mylst.append(lst[i])
        combi(mynum)
        mylst.pop()
def veri():
#비밀번호 검증
    for i in retlst:
        aeiou=0
        another=0
        for j in i:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                aeiou +=1
            else:
                another +=1
        if aeiou < 1 or another < 2: #자음 2개 미만, 모음 1개 미만
            anslst.remove(i)
retlst = []
mylst = []
mynum, num1 = map(int, input().split())
lst = sorted(list(map(str, input().split())))
combi(mynum)
retlst1 = copy.deepcopy(retlst)
for i in retlst1:#중복값 제거
    for j in i:
        if i.count(j) > 1:
            retlst.remove(i)
            break
anslst = copy.deepcopy(retlst)
veri()
for i in anslst:
    for j in i:
        print(j, end='')
    print()
#6C4를 모두 구해서 검증하는 방법
#배열을 담고 난 후 검증하는 방법