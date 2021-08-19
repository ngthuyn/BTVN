"""Bài 08: Viết chương trình đếm số lần xuất hiện 
các từ đơn trong một đoạn văn bản"""
str=input("Nhập đoạn văn: ")
dem=0
a=str.split(" ")
for i in range(len(a)):
    if len(a[i])==1: dem+=1
print( dem)
str.split()