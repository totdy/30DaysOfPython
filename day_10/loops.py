import sys
sys.path.insert(1, 'C:\\Users\\nazar\\Documents\\projects\\30DaysOfPython')

#1.1
for i in range(11):
    print(i)
i=0
while i < 10:
    print(i)
    i+=1

#1.2
for i in range(10,-1,-1):
    print(i)
i=10
while i > -1:
    print(i)
    i-=1
#1.3
tag = '#'
for i in range(8):
    print(tag)
    tag += ' #'
#1.4
for i in range(7):
    tag = '#'
    for i in range(7):
        tag += ' #'
    print(tag)
#1.5
for i in range(11):
    print('{} x {} = {}'.format(i,i,i*i))
#1.6
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)
#1.7
for i in range(101):
    if i % 2 == 0:
        print(i)
#1.8
for i in range(101):
    if i % 2 == 1:
        print(i)
#2.1
sum = 0
for i in range(101):
    sum += i
else:
    print('The sum of all numbers is %i.' %sum)
#2.2
sumEven, sumOdd = 0, 0
for i in range(101):
    if i % 2 == 0:
        sumEven += i
    else:
        sumOdd += i
else:
    print('The sum of all evens is {}. And the sum of all odds is {}.'.format(sumEven,sumOdd))
#3.1
from data.countries import *

landList = []
for country in countries:
    if(country.find('land') != -1):        
        landList.append(country)
else:
    print(landList)

#3.2
fruits = ['banana', 'orange','kiwi', 'mango', 'lemon']
i = 0
while i < int(len(fruits)/2):
    temp = fruits[i]
    fruits[i] = fruits[-i-1]
    fruits[-i-1] = temp
    i+=1
else:
    print(fruits)
#3.3
from data.countriesData import *

totalNumberOfLanguages = 0
for country in countriesData:
    if 'languages' in country:
        totalNumberOfLanguages += len(country['languages'])
else:
    print(totalNumberOfLanguages)
#3.4
spokenLanguages = {}
mostSpokenLanguage = ('',0)
for country in countriesData:
    if 'languages' in country:
        for language in country['languages']:
            if language in spokenLanguages:
                spokenLanguages[language] += 1
            else:
                spokenLanguages[language] = 1        
else:
    for language in spokenLanguages.items():
        if language[1] > mostSpokenLanguage[1]:
            mostSpokenLanguage = language
    else:
        print(mostSpokenLanguage)
#3.5 with AI 🤷‍♂️
#UPD now I understand it when sorted() tries to compare keys it actually calls lambda function thats gives it values instead of key and it compares values
most_populated_countries = sorted(countriesData, key=lambda x: x['population'], reverse=True)[0:10]
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")