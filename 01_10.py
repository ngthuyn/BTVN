from typing import get_args
class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_biggest_number(*args):
        a=sorted(args,reverse=1)
        print(f"The oldest dog is {a[0]} years old")


dog1=Dog("Fake",2)
print(f"{dog1.name} {dog1.age} tuổi")
dog2=Dog("Mickey",7)
print(f"{dog2.name} {dog2.age} tuổi")
dog3=Dog("Fuk",9)
print(f"{dog3.name} {dog3.age} tuổi")

Dog.get_biggest_number(1,2,3,4,6,7)
