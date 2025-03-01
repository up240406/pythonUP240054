#Day 2 Exercise 1 Data----------------
nombre = 'Angel Gael' #3
apellido = 'Trujillo Morones' #4
nombre_completo = nombre, apellido #5
pais = 'Mexico' #6
ciudad = 'Aguascalientes' #7
edad = 18 #8
año = 2025 #9
is_married = 'true' 
is_true = 'true' 
is_light_on = 'true' #12
A, B = 'si', 'no' #
#-------------------------------------
#1.Check the data type
print(type(nombre)) 
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type((A, B)))
#--------------------------------------
#2.Find the length of your first name
print(len(nombre)) 
#3.Compare the length of your first name and your last name
print(len(apellido))
#4.Declare 5 as num_one and 4 as num_two
num_one = 5 
num_two = 4
#5.Add num_one and num_two and assign the value to a variable total
total = num_one + num_two 
#6.Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two 
#7.Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two 
#8.Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two 
#9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two 
#10.Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#11.Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two 

print('4+5=',total) #5
print('4-5=',diff) #6
print('4*5=',product) #7
print('4/5=',division) #8
print('4%5=',remainder) #9
print('4**5=',exp) #10
print('4//5=',floor_division) #11

#12.The radius of a circle is 30 meters.
    #i.Calculate the area of a circle 
    #ii.Calculate the circumference of a circle 
    #iii.Take radius as user input and calculate the area.
radius = int(input('radius = '))
area_del_circulo = 3.14 * (radius ** 2)
circunferencia_del_circulo = 2*3.14*radius
print(area_del_circulo)
print(circunferencia_del_circulo)

#13.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_name = input('Name: ')
user_lastname = input('Last name: ')
user_country = input('Country: ')
age = input('age: ')

#14.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords') 