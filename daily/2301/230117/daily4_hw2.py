words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
stk=[]
for i in range(len(words)-1):
    if words[i] in stk:
        print(f"{i+1}번째 사람이 패배")
        break
    stk.append(words[i])
    if words[i][-1]==words[i+1][0]:
        continue
    else:
        print(f"{i+2}번째 사람이 패배!!")
        break