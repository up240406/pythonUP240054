age = int(18)
height = 1.77
comp = 5j
print (age)
print (height)
print (comp)

b = int(input('base = '))
h = int(input('height = '))
print ('the area is = ', 3*b*h)
side_a = int(input('ide a = '))
side_b = int(input('ide b = '))
side_c = int(input('ide c = '))
perimeter = side_a + side_b + side_c
print ('the perimeter equals', perimeter)

length = int(input('length = '))
width = int(input('width = '))
area_rec, perimeter_rec = width*length, 2*(length + width)
print('area is', area_rec, 'perimeter is', perimeter_rec)

radius = int(input('radius= '))
pi = 3.14
area_circ, circum = pi*radius**2, 2*pi*radius
print('area is', area_circ, 'circumference is', circum)

x = int(input('x= '))
slope = (5*x)-5
print(slope)

slope1 = (10-5)/(7-5)
print(slope1)

x = int(input('x= '))
y = (x**5)+(7*x)+4
print(y)

print(len('python') < len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'i hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
print(len('python'))
print(float(len('python')))
print(str(len('python')))

num = int(input ('Enter any number: ')) 
if((num % 2) == 0): print('even') 
else: print('The provided number is odd')

print(7//3 == 2.7)
print('10' == 10)
print(9.8 == 10)

hrs = int(input('hours: '))
rate = int(input('rate: '))
pay = hrs * rate 
print('payment: ',pay)

years = int(input('Number of years: '))
seconds = years*3600 
print('youve lived for: ', seconds)

for i in range(1,6):
    print(f'{i} {i**0} {i**2} {i**3}')