#1
dog = {}
#2
dog['name'] = 'Boba'
dog['color'] = 'white'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
#3
student = {
    'first_name': 'Boba',
    'last_name': 'Messi',
    'gender': 'male',
    'age': 24,
    'marital status': 'single',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Finland',
    'city': 'Helsinki',
    'address': 'Keskuskatu 42'
}
#4
print(len(student))
#5
print(type(student['skills']))
#6
student['skills'].append('HTML')
student['skills'].append('CSS')
#7
print(student.keys())
#8
print(student.values())
#9
print(student.items())
#10
del student['age']
#11
del student