import sys
sys.path.insert(1, 'C:\\Users\\nazar\\Documents\\projects\\30DaysOfPython')

#1.1
def add_two_numbers(a, b):
    return a + b
#1.2
def area_of_circle(r):
    return 3.14 * r * r
#1.3
def add_all_nums(*args):
    sum = 0
    for n in args:
        if type(n) == int:
            sum += n
        else:
            return "Error all arguments must bee numbers"            
    return sum
#1.4
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
#1.5
def check_season(month):
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
def calculate_slope(x1, y1, x2, y2):    
    slope = (y2 - y1) / (x2 - x1)    
    return slope
#1.7
from math import sqrt
def solve_quadratic_eqn(a, b, c):    
    xP = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    xN = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    return "X can be: %.2f or %.2f" %(xP, xN)
#1.8
def print_list(l):
    if type(l) != list:
        print("Error not a list")
        return

    for i in(l):
        print(i)
#1.9
def reverse_list(l):
    if type(l) != list:
        return "Error not a list"
    middleIndex = int(len(l)/2)
    for i in range(middleIndex):
        tmp = l[i]
        l[i] = l[-i-1]
        l[-i-1] = tmp
    return l
#1.10
def capitalize_list_items(l):
    if type(l) != list:
        return "Error not a list"
    for i in range(len(l)):
        if type(l[i]) == str:
            l[i] = l[i].capitalize()
    return l
#1.11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(l, item):
    if type(l) != list:
        return "Error not a list"
    l.append(item)
    return l
#1.12
def remove_item(l, item):
    if type(l) != list:
        return "Error not a list"
    l.remove(item)
    return l
#1.13
def sum_of_numbers(n):
    if type(n) != int:
        return "Error not a integer"
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
#1.14
def sum_of_odds(n):
    if type(n) != int:
        return "Error not a integer"
    sum = 0
    for i in range(n+1):
        if i % 2 == 1:
            sum += i
    return sum
#1.15
def sum_of_evens(n):
    if type(n) != int:
        return "Error not a integer"
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum
#2.1
def evens_and_odds(n):
    if type(n) != int or n < 0:
        return "Error not a integer or less than 0"
    
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
def factorial(n):
    if type(n) != int or n < 0:
        return "Error not a integer or less than 0"
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(10))
#2.3
def is_empty(p):
    if type(p) == int or type(p) == float:
        return "Error integer or float has no length"
    if len(p) == 0:
        return True
    else:
        return False
#2.4
def calculate_mean(l):
    if type(l) != list:
        return "Error not a list"
    sum = 0
    for i in l:
        if type(i) == int or type(i) == float:
            sum += i
    return sum/len(l)
print(calculate_mean([1,2,3,4,5]))

def calculate_median(l):
    if type(l) != list:
        return "Error not a list"
    l.sort()
    if len(l) % 2 == 0:
        return (l[int(len(l)/2)] + l[int(len(l)/2) - 1])/2
    else:
        return l[int(len(l)/2)]
print(calculate_median([1,2,3,4,5,6,7,8,9,10]))

def calculate_mode(l):
    if type(l) != list:
        return "Error not a list"

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

def calculate_range(l):
    if type(l) != list:
        return "Error not a list"
    
    rangeOfList = max(l) - min(l)
    return rangeOfList
print(calculate_range([14,19,20,24,25,28]))

def calculate_variance(l):
    if type(l) != list:
        return "Error not a list"
    
    mean = calculate_mean(l)
    variance = 0
    for i in l:
        variance += (i - mean)**2
    variance /= len(l)
    return variance
print(calculate_variance([14,19,20,24,25,28]))

def calculate_standard_deviation(l):
    if type(l) != list:
        return "Error not a list"
    
    variance = calculate_variance(l)
    return sqrt(variance)
print(calculate_standard_deviation([14,19,20,24,25,28]))

#3.1
def is_prime(n):
    if type(n) != int or n < 0:
        return "Error not a integer or less than 0"

    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
#3.2
def items_are_unique(l):
    if type(l) != list:
        return "Error not a list"
    
    if len(l) == len(set(l)):
        return True
    else:
        return False
print(items_are_unique([14,19,20,24,25,28]))
#3.3
def items_are_of_the_same_type(l):
    if type(l) != list:
        return "Error not a list"
    
    for i in l:
        if type(i) != type(l[0]):
            return False
    return True
print(items_are_of_the_same_type(['14',19,20,24,25,28]))
#3.5
from data.countriesData import *

def most_spoken_language():
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
print(most_spoken_language())
#3.6
def most_populated_countries():
    most_populated_countries = sorted(countriesData, key=lambda x: x['population'], reverse=True)[0:10]
    most_populated_countries_list = []
    for country in most_populated_countries:
        most_populated_countries_list.append((country['name'], country['population']))
    return most_populated_countries_list
print(most_populated_countries())