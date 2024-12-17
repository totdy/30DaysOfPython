#1
strings = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(strings))
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6 
print(company.upper())
#7 
print(company.lower())
#9
print(company[6:])
#10
print(company.find('Coding'))
#11
print(company.replace('Coding', 'Python'))
#13
print(company.split())
#14
brands = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(brands.split(','))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#20
print(company.lower().index('c'))
#21
print(company.lower().index('f'))
#22
print(company.lower().index('l'))
#27
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because ', ''))
#28
print(company.startswith('Coding'))
#29
print(company.endswith('Coding'))
#33
print('I am enjoying this challenge. \nI just wonder what is next.')
#34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
#35
radius = 10
print('radius = {}\narea = 3.14 * radius ** 2\nThe area of a circle with radius {} is {} meters square.'.format(radius, radius, 3.14 * radius ** 2))
#36
print('{} + {} = {}'.format(8, 6, 8 + 6))
print('{} - {} = {}'.format(8, 6, 8 - 6))
print('{} * {} = {}'.format(8, 6, 8 * 6))
print('%d / %d = %.2f'%(8, 6, 8 / 6))
print('{} % {} = {}'.format(8, 6, 8 % 6))
print('{} // {} = {}'.format(8, 6, 8 // 6))
print('{} ** {} = {}'.format(8, 6, 8 ** 6))