#1.1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need %s more years to learn to drive.'%(18 - age))
#1.2
yourAge = int(input('Enter your age: '))
myAge = 26
if yourAge > myAge:
    print('You are %s years older than me.'%(yourAge- myAge))
elif yourAge < myAge:
    print('I am %s years older than you.'%(myAge - yourAge))
else:
    print('We are the same age.')
#2.1
score = 76
if score >= 80 and score <= 100:
    print('Your grade is A.')
elif score >= 70 and score <= 79:
    print('Your grade is B.')
elif score >= 60 and score <= 69:
    print('Your grade is C.')
elif score >= 50 and score <= 59:
    print('Your grade is D.')
elif score >= 0 and score <= 49:
    print('Your grade is F.')
#2.2
Autumn = ('September', 'October', 'November')
Winter = ('December', 'January', 'February')
Spring = ('March', 'April', 'May')
Summer = ('June', 'July', 'August')
month = input('Enter a month: ').capitalize()
if month in Autumn:
    print('This is Autumn.')
elif month in Winter:
    print('This is Winter.')
elif month in Spring:
    print('This is Spring.')
elif month in Summer:
    print('This is Summer.')
else:
    print('Not a valid month.')
#2.3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').lower()
if fruit in fruits:    
    print('That fruit is in the list.')
else:
    fruits.append(fruit)
    print(fruits)
#3.1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

frontEnd = ['JavaScript', 'React']
backEnd = ['Node', 'MongoDB', 'Python']

if 'skills' in person:
    print(person['skills'][int(len(person['skills']) / 2)])

    if 'Python' in person['skills']:
        print('You have Python skill')

    if person['skills'] == frontEnd:
        print('He is a front-end developer')
    elif person['skills'] == backEnd:
        print('He is a back-end developer')
    elif person['skills'] == frontEnd + backEnd:
        print('He is a full-stack developer')
    else:
        print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print('{} lives in {}. He is married.'.format(person['first_name']+' '+person['last_name'], person['country']))