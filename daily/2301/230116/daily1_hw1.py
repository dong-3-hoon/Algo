score = {
    'python': 80,
    'django': 89,
    'web': 83
}
stk=0#점수 저장용
cnt=0#과목 갯수
score['algorithm']=90 #새로운 key: value 추가
score['python']=85#기존 key에서 value 변경
for i in score.values():
    stk+=i
    cnt+=1
print(stk/cnt)