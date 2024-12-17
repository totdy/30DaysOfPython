from math import sqrt
"""
#1
age = 0
#2
height = 0.0
#3
complexNumber = 0j
#4
print('Calculate an area of the triangle')
base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is '+str(area))
#5
print('Calculate the perimeter of the triangle')
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = float(input('Enter side C: '))
perimeter = a + b + c
print('The perimeter of the triangle is '+str(perimeter))
#6
print('Calculate an area of the rectangle')
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = 2 * (length + width)
print('The area of the rectangle is '+str(area))
#7
print('Calculate an area and circumference of the circle ')
radius = float(input('Enter radius: '))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print('The area is '+str(area)+' and circumference is '+str(circumference))
#8
print('Calculate the slope by x1')
x1 = float(input('Enter x: '))
y1 = 0
x2 = 0
y2 = 2 * x1 - 2
slope1 = (y2 - y1) / (x2 - x1)
print('The slope is '+str(slope1))
#9
print('Calculate the slope by x1,y1 and x2,y2')
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y1: '))
slope2 = (y2 - y1) / (x2 - x1)
euclidean = sqrt((x1-x2)**2+(y1-y2)**2)
print('The slope is '+str(slope2)+' and euclidean distance is '+str(euclidean))
#10
print(slope1==slope2)
#12
"""
print(len('python') != len('dragon'))
#13
print('on' in 'python' and 'on' in 'dragon')
#14
print('jargon ' in 'I hope this course is not full of jargon')
#15
print('on' not in 'python' and 'on' not in 'dragon')
#16
print(str(float(len('python'))))
#17
num = 3
if(num % 2 == 0):
    print('The number is even')
else:    
    print('The number is odd')
#18
print((7//3) == int(2.7))
#19
print(type('10') == type(10))
#20
print(int(float('9.8')) == 10)
#23
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')