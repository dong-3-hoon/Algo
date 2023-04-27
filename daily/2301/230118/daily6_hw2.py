# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

#알파벳을 사전 순서대로 정렬
words=['eat','tea','tan','ate','nat','bat']
#에너그램 그룹 딕셔너리로 묶기
anagrams={}

#에너그램 -> 순서를 섞어서 다른 문자열 만들기
#사전순으로 정렬해버리면 다 똑같아짐
#정렬 후 비교해서 같으면 같은 애너그램 그룹에 넣음

for word in words:
    #단어를 사전순으로 정렬
    #print(list(sorted(word)))#정렬 후 리스트를 리턴
    temp=sorted(word)
    #정렬 결과가 리스트가 되어버리니까 디시 문자열로 변경
    temp = "".join(temp)
    #print(temp)
    #정렬 결과를 key로 저장하고 리스트로 묶어줌
    #정렬 결과가 이미 딕셔너리에 존재하는지 검사
    if anagrams.get(temp):
        anagrams[temp].append(word)
    
    #존재하지 않으면 새로운 리스트를 만들어서 추가
    else:
        anagrams[temp] = [word]
print(anagrams.values())
        
    #print(anagrams)
    #print(anagrams.values())
'''
arr=['eat','tea','tan','ate','nat','bat']
lst1=[]
lst2=[]
stk=[]
save=[]
ooutput=[]
cnt=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            continue
        else:#여기서 단어끼리 비교하는 건데
            for a in arr[i]:
                lst1.append(a)
            for b in arr[j]:
                lst2.append(b)
            #여기서 문자 하나씩 비교
            for word1 in lst1:
                for word2 in lst2:
                    if word1==word2:
                        cnt+=1
                
            #같은 단어의 카운트가 길이와 같을 때 stk에 추가
            if cnt==len(lst1):
                if lst1 not in stk:
                    stk.append(lst1)
                if lst2 not in stk:
                    stk.append(lst2)
            cnt=0
            lst1=[]
            lst2=[]
    #없는거면 ooutput에 추가
    if stk not in ooutput:
        ooutput.append(stk)
    print(ooutput)
    stk=[]
'''
