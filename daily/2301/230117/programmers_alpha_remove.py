def solution(my_string, letter):
    answer = ''
    lst1=[]
    for i in my_string:
        if i==letter:
            continue
        else:
            lst1.append(i)
    for i in lst1:
        answer+=i
    return answer