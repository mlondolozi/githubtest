print("Hello world")
for x in range(10):
    print(f'testing {x}')


#dictionaries
person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_marred':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }

print(person['address'])

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

print()
person['first_name'] = 'Eyob'
person['age'] = 252
print(person)

print()
print(person.items())
print()
print(person.values())