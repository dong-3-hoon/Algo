class Stack:
    def __init__(self, lst):
        self.lst = lst
    def empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False
    def top(self):
        if len(self.lst)==0:
            return None
        else:
            return self.lst[-1]
    def pop(self):
        if len(self.lst)==0:
            return None
        else:
            last = self.lst[-1]
            self.lst.remove(last)
            return last
    def push(self, number):
        self.lst.append(number)
    def __repr__(self):
        return self.lst

p1 = Stack([])
print(p1.empty())
print(p1.top())
print(p1.pop())
print(p1.push(1))
print(p1.__repr__())

p1 = Stack([1,2,3])
print(p1.empty())
print(p1.top())
print(p1.pop())
print(p1.push(1))
print(p1.__repr__())