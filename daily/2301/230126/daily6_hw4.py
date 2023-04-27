entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']
'''
entry_dict={}
exit_dict={}
lst=[]
cnt=0
#엔트리 레코드 리스트에서 사람의 이름 당 들어간 횟수를 기록
for i in entry_record:
    if i not in entry_dict.keys():
        entry_dict[i]=1
    else:
        entry_dict[i]+=1
#엑시트 레코드 리스트에서 사람의 이름 당 나간 횟수를 기록
for i in exit_record:
    if i not in exit_dict.keys():
        exit_dict[i]=1
    else:
        exit_dict[i]+=1
print('입장 기록이 많은 Top3')
for i in entry_dict.values():
    lst.append(i)
lst.sort(reverse=True)
for i in lst:
    for j in entry_dict:
        if entry_dict[j]==i:
            cnt+=1
            print(f'{j} {i}회')
            break
    if cnt==3:
        break
print('출입 기록이 수상한 사람')
for i in entry_dict:
    for j in exit_dict:
        if i==j and entry_dict[i] != exit_dict[j]:
            if entry_dict[i]>exit_dict[j]:
                print(f'{i}는 입장 기록이 {entry_dict[i]-exit_dict[j]}회 더 많아 수상합니다.')
            else:
                print(f'{i}는 퇴장 기록이 {exit_dict[j]-entry_dict[i]}회 더 많아 수상합니다.')
'''
entry_dict={}
exit_dict = {}

for name in entry_record:
    #딕셔너리에 이름이 해당하는 키가 있다.
    if entry_dict.get(name):
        entry_dict[name] += 1
    #딕셔너리에 해당하는 키가 없다.
    else:
        entry_dict[name] = 1

for name in exit_record:
    #딕셔너리에 이름이 해당하는 키가 있다.
    if exit_dict.get(name):
        exit_dict[name] += 1
    #딕셔너리에 해당하는 키가 없다.
    else:
        exit_dict[name] = 1
#입장횟수 제일 많은 사람 위에서부터 Top3
#내림차순 정렬을 해준 다음 처음에서 3명 뽑으면 됨
#dict.item은 정렬이 가능하게 해준다 - dict의 key, value를 튜플로 묶어준다.
sorted_entry = sorted(entry_dict.items(), key=lambda item: item[1], reverse=True)

for name, count in sorted_entry[:3]:
    print(f'{name} : {count}회 입장')

#출입기록이 수상한 사람의 목록
#|입장횟수 -퇴장횟수| != 0

for name, count in entry_dict.items():
    diff = count - exit_dict[name]
    if diff != 0:
        print(f'{name}은 수상한 사람입니다.{diff}')        
