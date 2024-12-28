import sys
sys.path.insert(1, 'C:\\Users\\nazar\\Documents\\projects\\30DaysOfPython')

from math import sqrt
from data.countriesData import *

#1.1
def add_two_numbers(a:int|float, b:int|float):
    return a + b
#1.2
def area_of_circle(r:int|float):
    return 3.14 * r * r
#1.3
def add_all_nums(*args:int|float):
    sum = 0
    for n in args:        
        sum += n        
    return sum
#1.4
def convert_celsius_to_fahrenheit(c:int|float):
    f = (c * 9/5) + 32
    return f
#1.5
def check_season(month:str):
    Autumn = ('September', 'October', 'November')
    Winter = ('December', 'January', 'February')
    Spring = ('March', 'April', 'May')
    Summer = ('June', 'July', 'August')
    month = month.capitalize()
    if month in Autumn:
        season = 'This is Autumn.'
    elif month in Winter:
        season = 'This is Winter.'
    elif month in Spring:
        season = 'This is Spring.'
    elif month in Summer:
        season = 'This is Summer.'
    else:
        season = 'Not a valid month.'
    return season
#1.6
def calculate_slope(x1:int|float, y1:int|float, x2:int|float, y2:int|float):    
    slope = (y2 - y1) / (x2 - x1)    
    return slope
#1.7
def solve_quadratic_eqn(a:int|float, b:int|float, c:int|float):    
    xP = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    xN = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    return "X can be: %.2f or %.2f" %(xP, xN)
#1.8
def print_list(l:list):
    for i in l:
        print(i)
#1.9
def reverse_list(l:list):    
    middleIndex = int(len(l)/2)
    for i in range(middleIndex):
        tmp = l[i]
        l[i] = l[-i-1]
        l[-i-1] = tmp
    return l
#1.10
def capitalize_list_items(l:list[str]):
    for i in range(len(l)):        
        l[i] = l[i].capitalize()
    return l
#1.11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(l:list, item:str):    
    l.append(item)
    return l
#1.12
def remove_item(l:list, item:str):    
    l.remove(item)
    return l
#1.13
def sum_of_numbers(n:int):    
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
#1.14
def sum_of_odds(n:int):    
    sum = 0
    for i in range(n+1):
        if i % 2 == 1:
            sum += i
    return sum
#1.15
def sum_of_evens(n:int):
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum
#2.1
def evens_and_odds(n:int):
    if n < 0:
        return "Error less than 0"    
    evens = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds
evens, odds = evens_and_odds(100)
print('The number of odds are {}. \nThe number of evens are {}.'.format(odds, evens))
#2.2
def factorial(n:int):
    if n < 0:
        return "Error less than 0"
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(10))
#2.3
def is_empty(p):
    if type(p) == int|float:
        return "Error integer or float has no length"
    elif len(p) == 0:
        return True
    else:
        return False
#2.4
def calculate_mean(l:list[int|float]):    
    sum = 0
    for i in l:        
        sum += i
    return sum/len(l)
print(calculate_mean([1,2,3,4,5]))

def calculate_median(l:list[int|float]):    
    l.sort()
    if len(l) % 2 == 0:
        return (l[int(len(l)/2)] + l[int(len(l)/2) - 1])/2
    else:
        return l[int(len(l)/2)]
print(calculate_median([1,2,3,4,5,6,7,8,9,10]))

def calculate_mode(l:list[int|float]):
    numCount = {}
    for i in l:
        if i in numCount:
            numCount[i] += 1
        else:
            numCount[i] = 1

    sortedCount = sorted(numCount.items(), key=lambda x: x[1], reverse=True)
    
    maxCount = [sortedCount[0]]
    for i in range(1, len(sortedCount)):
        if i+1 < len(sortedCount) and sortedCount[i][1] == maxCount[0][1]:
            maxCount.append(sortedCount[i])
        else:
            break
    return maxCount
print(calculate_mode([1,2,3,4,5,6,7,8,9,10]))

def calculate_range(l:list[int|float]):
    rangeOfList = max(l) - min(l)
    return rangeOfList
print(calculate_range([14,19,20,24,25,28]))

def calculate_variance(l:list[int|float]):
    mean = calculate_mean(l)
    variance = 0
    for i in l:
        variance += (i - mean)**2
    variance /= len(l)
    return variance
print(calculate_variance([14,19,20,24,25,28]))

def calculate_standard_deviation(l:list[int|float]):
    variance = calculate_variance(l)
    return sqrt(variance)
print(calculate_standard_deviation([14,19,20,24,25,28]))

#3.1
def is_prime(n:int):
    if n < 0:
        return "Error less than 0"

    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
#3.2
def items_are_unique(l:list):    
    if len(l) == len(set(l)):
        return True
    else:
        return False
print(items_are_unique([14,19,20,24,25,28]))
#3.3
def items_are_of_the_same_type(l:list):
    for i in l:
        if type(i) != type(l[0]):
            return False
    return True
print(items_are_of_the_same_type(['14',19,20,24,25,28]))
#3.5
def most_spoken_language(countriesData:list):
    spokenLanguages = {}
    for country in countriesData:
        if 'languages' in country:
            for language in country['languages']:
                if language in spokenLanguages:
                    spokenLanguages[language] += 1
                else:
                    spokenLanguages[language] = 1
    mostSpokenLanguages = sorted(spokenLanguages.items(), key=lambda x: x[1], reverse=True)[0:10]
    return mostSpokenLanguages
print(most_spoken_language(countriesData))
#3.6
def most_populated_countries(countriesData:list):
    most_populated_countries = sorted(countriesData, key=lambda x: x['population'], reverse=True)[0:10]
    most_populated_countries_list = []
    for country in most_populated_countries:
        most_populated_countries_list.append((country['name'], country['population']))
    return most_populated_countries_list
print(most_populated_countries(countriesData))