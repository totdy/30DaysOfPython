#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])
#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([i for lvl1 in list_of_lists for lvl2 in lvl1 for i in lvl2])
#3
print([(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)])
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[countryCityTuple[0].upper(), countryCityTuple[0][0:3].upper(), countryCityTuple[1].upper()] for countryCityList in countries for countryCityTuple in countryCityList])
#5
print([{'country': countryCityTuple[0].upper(), 'city': countryCityTuple[1].upper()} for countryCityList in countries for countryCityTuple in countryCityList])
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([namesTuple[0] + ' ' + namesTuple[1] for namesList in names for namesTuple in namesList])
#7 calculate slope
slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(slope(1,1,2,2))