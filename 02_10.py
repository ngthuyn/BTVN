"""Bài 02. Xem code đã có trong file btvn_02_pet.py (đính kèm bên dưới). Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Hãy tạo ra class Pet để chứa các đối tượng của class Dog, class Pet này độc lập với class Dog (hay Pet ko kế thừa từ Dog)
        - Sau đó, tạo 4 đối tượng kiểu Dog và gán thành thuộc tính của 1 đối tượng kiểu Pet
            name        age
            Tom          6
            Jerry        9
            Butt         3
            Wine         1
        - Code đoạn chương trình để in ra được như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course."""

class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'
 

class Pets():
    dogs=[]
    
    def exercise_2(self):
        Pets.dogs=[dog1,dog2,dog3,dog4]
        print(self.dogs[0],end=". ")
        print(self.dogs[1],end=". ")
        print(self.dogs[2],end=". ")
        print(self.dogs[3])


# tạo list dogs ở hàm excercise_2
dog1=Dog("Tom",6).description()
dog2=Dog("Jerry",9).description()
dog3=Dog("Butt",3).description()
dog4=Dog("Wine",1).description()

# in ra yêu cầu của exercise_2
print("I have 4 dogs.")
dog=Pets().exercise_2()
print(f"And they're all {Dog.species}, of course.")
