import sys

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

print()
a = 3
# first condition met, 'A is positive' will be printed
print('A is positive') if a > 0 else print('A is negative') 

print()
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue

    # for short hand conditions need both if and else statements
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") 
    
print('outside the loop')

print()
print(sys.version)

print()
numbers = [(i, i * i) for i in range(11)]
print(numbers)    

print()
# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)