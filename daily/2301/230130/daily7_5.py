import random

class ClassHelper:
    def __init__(self, name):
        self.name = name
    def pick(self, num):
        pickk = random.sample(ch.name, num)
        return pickk
    def match_pair(self):
        pair = []
        last_pair = []
        while len(ch.name)>0:
            if len(ch.name)==3:
                last_pair.append(ch.name)
                return last_pair
            else:
                a = random.choice(ch.name)
                pair.append(a)
                ch.name.remove(a)
                a = random.choice(ch.name)
                pair.append(a)
                ch.name.remove(a)
                if len(pair)==2:
                    last_pair.append(pair)
                    pair = []
        return last_pair


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
