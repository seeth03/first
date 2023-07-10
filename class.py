class Dog:
    name = ""
    age = ""

Dog1 = Dog
Dog1.name = 'tue'
Dog1.age = 10

Dog2 = Dog
Dog2.name = 'yue'
Dog2.age = 15

print(f'{Dog1.name} is {Dog1.age} yeras old')
print(f'{Dog2.name} is {Dog2.age} years old')