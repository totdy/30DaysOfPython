# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.1
print(len(it_companies))
#1.2
it_companies.add('Twitter')
#1.3
it_companies.update({'Meta','iS'})
#1.4
it_companies.discard('Facebook')
#2.1
AB = A.union(B)
#2.2
print(A.intersection(B))
#2.3
print(A.issubset(B))
#2.4
print(A.isdisjoint(B))
#2.5
A.update(B)
B.update(A)
#2.6
print(A.symmetric_difference(B))
#2.7
del A, B
#3.1
ages = set(age)
print(len(ages), len(age)) # age is bigger cause it has duplicates
#3.2
# mutable can be changed, immutable can't
# String is a combination of immutable chars, only reasignable
# List is a combination of ordered mutable items
# Tuple is a combination of ordered immutable items, only reasignable
# Set is a combination of unique unordered mutable items
#3.3
txt = 'I am a teacher and I love to inspire and teach people'
txt_set = set(txt.split())
print('"{}" has {} unique words'.format(txt, len(txt_set)))