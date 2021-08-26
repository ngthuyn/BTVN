"""Bài 04. Xem code đã có trong file btvn_04_dog_walking.py.
    Giải quyết yêu cầu sau:
        - Thêm method walk() vào class Pet và Dog. Khi gọi đến hàm walk() trong Pet thì vỡi mỗi đối tượng của Dog trong Pet
        sẽ gọi đến hàm walk() tương ứng.
        - Viết đoạn chương trình để in ra như sau:
            Tom is walking!
            Jerry is walking!
            Butt is walking!"""



class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def walk(self,walking):
        self.walking=walking
        return f'{self.name} is {self.walking}!'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Pets():
    dogs=[]
   
    def walk(self):
        Pets.dogs=[dog1,dog2,dog3]
        for i in range(3):
            print(self.dogs[i])

  
# tạo list dogs ở hàm excercise_2
dog1=Dog("Tom",6).walk("walking")
dog2=Dog("Jerry",9).walk("walking")
dog3=Dog("Butt",3).walk("walking")
#dog4=Dog("Wine",1).walk("walking")

# in theo yêu cầu
dog=Pets().walk()
