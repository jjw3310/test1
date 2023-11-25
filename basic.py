
person = {
'firstName': 'Jane',
'age': 25,
'occupation': 'Engineer'
}

print(person['firstName'])
person['age'] = 26
print(person['age'])

person['company'] = 'XYZ Corp.'
print(person)

del person['occupation']
print(person)

import math

print(math.sqrt(25))

print(math.e)

temperature = 20

if temperature >= 30:
    print("It's hot.")
else:
    print("It's not hot.")

animals = ['cat', 'dog', 'rabbit']

for animal in animals:
    print(animal)


i = 0

while i < 3:
    print(i)
    i += 1


try:
    result = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Exception handling is complete.")