# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0
class Calc:
    def calculator(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        if op =='+':
            print(num1+num2)
        elif op == '-':
            print(num1-num2)
        elif op == '*':
            print(num1*num2)
        else:
            if num2 == 0:
                print('0으로 나눌 수 없습니다')
            else:
                print(num1/num2)
c1 = Calc()

c1.calculator(1, '+', 2)
c1.calculator(2, '-', 1)
c1.calculator(3, '*', 4)
c1.calculator(3, '/', 0)
c1.calculator(3, '/', 1)