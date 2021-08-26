"""Bài 03. Sử dụng tiếp file btvn_02_pet.py sau khi đã code xong Bài 02.
    Giải quyết yêu cầu sau:
        - Thêm thuộc tính is_hungry = True cho class Dog
        - Thêm một method eat() để thay đổi giá trị cho is_hungry thành False khi nó được gọi đến
        - Kiểm tra và in ra
            My dogs are not hungry.
        nếu như tất cả các Dog trong Pet đều có is_hungry = False, ngược lại thì in ra
            My dogs are hungry.
        - Cuối cùng có thể in ra được kiểu như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.
            My dogs are not hungry"""


class Dog:
    species = 'mammal'
    is_hungry = True
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'
    
    def eat(self):
        self.is_hungry = False
        return self.is_hungry

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

    def check_is_hungry(self):
        Pets.dogs=[dog1,dog2,dog3,dog4] # list này chứa phần tử là  True or False
        dem=0 
        for i in range(4):
            if self.dogs[i]==False: dem+=1
        if dem==4: print("My dogs are not hungry.")
        else:
            print("My dogs are hungry.")


# tạo list dogs ở hàm excercise_2
dog1=Dog("Tom",6).description()
dog2=Dog("Jelly",9).description()
dog3=Dog("Butt",3).description()
dog4=Dog("Wine",1).description()

# in ra yêu cầu của exercise_2
print("I have 4 dogs.")
dog=Pets()
dog.exercise_2()
print(f"And they're all {Dog.species}, of course.")

# tạo list dogs ở hàm check_is_hungry
dog1=Dog("Tom",6).eat()
dog2=Dog("Jerry",9).eat()
dog3=Dog("Butt",3).eat()
dog4=Dog("Wine",1).eat()

#phần in ra : My dogs are not hungry   
dog=Pets().check_is_hungry()

