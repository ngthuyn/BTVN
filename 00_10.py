"""Bài 00. Viết một chương trình để lấy ra tên class của một object?"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

person_1=Person("Hường",20)
#print(f"{person_1.name} {person_1.age} tuổi")
print(person_1.__class__)
