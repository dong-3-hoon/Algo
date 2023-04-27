class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle(Point):
    def __init__(self, p1, p2):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
    def get_area(self):
        return ((self.x2-self.x1)*(self.y1-self.y2))

    def get_perimeter(self):
        return (2*((self.x2-self.x1)+(self.y1-self.y2)))
    

    def is_square(self):
        if self.x2-self.x1 == self.y1-self.y2:
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True