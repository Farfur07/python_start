import math
import fractions

print('Enter values of triangle sides: ')
a = int(input('a = '))
b = int(input('b= '))
c = int(input('c= '))

h = a + b + c

# Semi Perimeter
s = fractions.Fraction(h, 2)

t_area = (math.sqrt(s*(s - a)*(s - b)*(s - c)))

print('Triangle area= ', round(t_area, 1))
