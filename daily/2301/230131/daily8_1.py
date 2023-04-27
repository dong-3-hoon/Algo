import copy
participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
lst = copy.deepcopy(participants)
for i in participants:
    if len(lst) == 1 or len(lst) == 0:
        break
    if participants.count(i) == 2:
        lst.remove(i)
        lst.remove(i)
print(lst)
