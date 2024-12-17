#1
#Day 2: 30 Days of python programming
first_name = 'Boba'
last_name = 'Messi'
full_name = first_name + ' ' + last_name
country = 'Finland'
city = 'Helsinki'
age = 24
year = 2022
is_married = False
is_true = True
is_light_on = True
a, b, c, d, = 'a', 'b', 'c', 'd'
#2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
#2.12
radius = 30
#2.12.1
area_of_circle = 3.14 * radius ** 2
#2.12.2
circum_of_circle = 2 * 3.14 * radius
#2.12.3
radius = float(input('Input the radius to calculate the area: '))
print(3.14 * radius ** 2)
#2.13
first_name = input('Your first name: ')
last_name = input('Your last name: ')
country = input('Your country: ')
age = int(input('Your age: '))
#2.14
help('keywords')