#1.1
from random import choice, randint, shuffle
from string import ascii_letters, digits

def random_user_id(n):
    randomChars = ''
    for i in range(n): 
        randomChars += choice(ascii_letters + digits)
    return randomChars
print(random_user_id(6))

#1.2
def user_id_gen_by_user():
    numOfUsers = int(input('Enter number of users: '))
    sizeOfId = int(input('Enter size of ID: '))
    result = []
    for i in range(numOfUsers):
        result.append(random_user_id(sizeOfId))
    return result
#print(user_id_gen_by_user())
#1.3
def rgb_color_gen():
    return 'rgb({},{},{})'.format(randint(0,255),randint(0,255),randint(0,255))
print(rgb_color_gen())
#2
def generate_colors (colorType, numOfColors):
    result = []
    if colorType == 'hexa':
        for i in range(numOfColors):
            randomChars = '#'
            for i in range(6):
                randomChars += choice(ascii_letters[0:6] + digits)
            result.append(randomChars)
    elif colorType == 'rgb':
        for i in range(numOfColors):
            result.append('rgb({},{},{})'.format(randint(0,255),randint(0,255),randint(0,255)))
    return result
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
#3.1
def shuffle_list(l):
    if type(l) != list:
        return "Error not a list"
    shuffle(l)
    return l
print(shuffle_list(['14',19,20,24,25,28]))
#3.2
def random_unique_numbers():
    result = []
    while len(result) < 7:
        randNum = randint(0,9)
        if randNum not in result:
            result.append(randNum)
        else: continue
    return result
print(random_unique_numbers())