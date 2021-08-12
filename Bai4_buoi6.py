"""Bài 04. Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím."""
list=['apple','banana','cherry',"orange", "kiwi", "melon", "mango"]
while True:
    d=int(input("Nhập vào độ dài phần đầu:"))
    if 0<d<len(list):
        print(list[:d])
        print(list[d:])
        break
    else: print("Nhập lại!")
