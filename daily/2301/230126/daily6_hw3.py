def count_vowels(strr):
    cnt=0
    for i in strr:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            cnt+=1
    print(cnt)
count_vowels('apple') #=> 2
count_vowels('banana') #=> 3