"""Bài 00. Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc."""
import  random
list=[1,2,3,4,5,'a','b','c','d','$','@']
list1 = []
for i in range(5):
    list1.append(random.choice(list))
print(list1)