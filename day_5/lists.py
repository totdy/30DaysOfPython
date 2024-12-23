import sys
sys.path.insert(1, 'C:\\Users\\nazar\\Documents\\projects\\30DaysOfPython')

#1.1
list = []
#1.2
list = [1,2,3,4,5]
#1.3
print(len(list))
#1.4
print(list[0], list[int(len(list)/2)], list[-1])
#1.5
mixed_data_type = ['Boba',26,200,'Single','Finland']
#1.6
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#1.7
print(it_companies)
#1.8
print(len(it_companies))
#1.9
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])
#1.11
it_companies.append('Meta')
#1.12
it_companies.insert(int(len(it_companies)/2),'iS')
#1.13
it_companies[1] = it_companies[1].upper()
#1.14
print('#1.; '.join(it_companies))
#1.15
print('Meta' in it_companies)
#1.16
it_companies.sort()
#1.17
it_companies.sort(reverse=True)
#1.18
print(it_companies[0:3])
#1.19
print(it_companies[-3:])
#1.20
print(it_companies[int(len(it_companies)/2)])
#1.21
it_companies.pop(0)
#1.22
it_companies.pop(int(len(it_companies)/2))
#1.23
it_companies.pop()
#1.24
it_companies.clear()
#1.25
del it_companies
#1.26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
#1.27
full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Redux')+1, 'SQL')
print(full_stack)
#2.1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#2.2
ages.sort()
minAge,maxAge = ages[0],ages[-1]
print('Min age {} and Max age {}'.format(minAge,maxAge))
#2.3
print('Middle age {}'.format(ages[int(len(ages)/2)]))
#2.4
avarageAge = sum(ages)/len(ages)
#2.5
rangeAge = max(ages) - min(ages)
#2.6
print(abs(minAge - avarageAge) == abs(maxAge - avarageAge))
#3.1
from data.countries import *

middleIndex = int(len(countries)/2)
print(countries[middleIndex])
#3.2
if(len(countries)%2 == 0):
    print(len(countries[0:middleIndex]), len(countries[middleIndex:]))
else:
    print(len(countries[0:middleIndex]), len(countries[middleIndex+1:]))
