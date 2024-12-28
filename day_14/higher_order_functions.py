import sys
sys.path.insert(1, 'C:\\Users\\nazar\\Documents\\projects\\30DaysOfPython')

from data.countries import *
from data.countriesData import *
from functools import reduce

countriesLocal = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1.1
# map iterates over a list and applies defined function to each element and returns a list 
# filter iterates over a list and compares each element with defined function and returns a list
# reduce iterates over a list and applies defined function to each element and returns a single result
#1.2
# I did not get it yet
#1.3
# ? 
#1.4
for country in countriesLocal:
    print(country)
#1.5
for name in names:
    print(name)
#1.6
for number in numbers:
    print(number)
#2.1
newCountries = list(map(lambda country : country.upper(), countriesLocal))
print(newCountries)
#2.2
newNumbers = list(map(lambda number : number**2, numbers))
print(newNumbers)
#2.3
names = list(map(lambda name : name.upper(), names))
print(names)
#2.4
def hasLand(country:str):
    if country.find('land') != -1:
        return True    
    return False
landCountries = list(filter(hasLand, countriesLocal))
print(landCountries)
#2.5
def hasSixChar(country:str):
    if len(country) == 6:
        return True    
    return False
sixCharCountries = list(filter(hasSixChar, countriesLocal))
print(sixCharCountries)
#2.7
eCountries = list(filter(lambda country : country.startswith('E'), countriesLocal))
print(eCountries)
#2.8
sixCharStartsWithENames = list(map(lambda name : name.upper(), filter(hasSixChar, filter(lambda name : name.startswith('E'), names))))
print (sixCharStartsWithENames)
#2.9
def isString(s):
    if type(s) == str:
        return True
    return False
def get_string_lists(l:list):
    onlyStrings = list(filter(isString, l))
    return onlyStrings
print(get_string_lists([1, '2', 3, '4', 5, '6', 7, '8', 9, '10']))
#2.10
def add_two_nums(x, y):
    return int(x) + int(y)
print(reduce(add_two_nums, numbers))
#2.11
print('{} are north European countries'.format(reduce(lambda x,y : x + ', ' + y, countriesLocal)))
#2.12
def hasPattern(pattern:str, s:str):
    if s.lower().find(pattern) != -1:
        return True    
    return False
def categorize_countries(pattern:str, l:list[str]):    
    result = list(filter(lambda country : hasPattern(pattern,country), l))
    return result
print(categorize_countries('land', countries))
print(categorize_countries('ia', countries))
print(categorize_countries('island', countries))
print(categorize_countries('stan', countries))
#2.13
def countriesByStartingLetter(l:list[str]):
    result = {}
    for country in l:
        if country[0:1] in result:
            result[country[0:1]] += 1
        else:
            result[country[0:1]] = 1
    return result
print(countriesByStartingLetter(countries))
#2.14
def get_first_ten_countries(l:list[str]):
    return l[0:10]
print(get_first_ten_countries(countries))
#2.15
def get_last_ten_countries(l:list[str]):
    return l[-10:]
print(get_last_ten_countries(countries))
#3.1
print(sorted(countriesData, key=lambda country : country['name']))
print(sorted(countriesData, key=lambda country : country['capital']))
print(sorted(countriesData, key=lambda country : country['population'], reverse=True))
#3.2
print(sorted(countriesData, key=lambda country : len(country['languages']), reverse=True)[0:10])
#3.3
print(sorted(countriesData, key=lambda country : country['population'], reverse=True)[0:10])