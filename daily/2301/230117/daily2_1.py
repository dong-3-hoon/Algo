a = 3
b = 6
c = - 5
answer1, answer2=0, 0
answer1=(-b-(b*b-4*a*c)**(1/2))/(2*a)
answer2=(-b+(b*b-4*a*c)**(1/2))/(2*a)
answer=(round(answer1, 3), round(answer2, 3))
print(answer)

'''
import numpy as numpy
a=1
b=0
c=-4
coeff=[a,b,c]

lower_x, upper_x=np,roots(coeff)
print(round(lower_x, 4), round(upper_x, 4))
'''