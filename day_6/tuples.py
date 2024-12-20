#1.1
tuple = ()
#1.2
brotherHood = ('Boba', 'Messi', 'Ronaldo', 'Neymar')
sisterHood = ('Shakira','Gaga','Ronda', 'Xena')
#1.3
siblings = brotherHood + sisterHood
#1.4
print(len(siblings))
#1.5
family = siblings + ('Mom', 'Dad')
#2.1
print('Siblings: {}, Parents: {}'.format(family[0:len(siblings)], family[-2:]))
#2.2
fruits = ('apple', 'banana', 'cherry')
vegetables = ('tomato', 'potato', 'carrot')
animalProducts = ('milk', 'cheese', 'meet')
food_stuff_tp = fruits + vegetables + animalProducts
#2.3
food_stuff_lt = list(food_stuff_tp)
#2.4
middleIndex = int(len(food_stuff_lt)/2)
print('Middle food: {}'.format(food_stuff_lt[middleIndex]))
#2.5
print('First three food: {}'.format(food_stuff_lt[0:3]))
print('Last three food: {}'.format(food_stuff_lt[-3:]))
#2.6
del food_stuff_tp
#2.8
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)