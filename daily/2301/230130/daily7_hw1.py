class Doggy:
    num_of_dogs = 0
    birth_of_dogs =0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    def __del__(self): #소멸자
        Doggy.num_of_dogs -= 1
    def bark():
        if Doggy.num_of_dogs > 0:
            print('멍멍')
        else:
            print('개가 없습니다')
    def get_status():
        print(f'태어난 개의 숫자: {Doggy.birth_of_dogs}, 현재 개의 숫자: {Doggy.num_of_dogs}')

Doggy.bark()
dog1 = Doggy('do1', 'yok')
dog2 = Doggy('do2', 'pudle')

Doggy.bark()
Doggy.get_status()
del dog1
Doggy.bark()
Doggy.get_status()
del dog2
Doggy.get_status()
Doggy.bark()