"""Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một string được nhập từ bàn phím"""
str=input("Nhập vào chuỗi kí tự:")
c=[]
for i in range(len(str)): 
    if str[i] not in c:
        c.append(str[i])
        print(f"số lần {str[i]} xuất hiện trong chuỗi {str}: {str.count(str[i])}")
