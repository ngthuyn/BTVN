"""Bài 06. Viết chương trình
    1. Nhập vào 1 chuỗi từ bàn phím
    2. Nhập vào 1 ký tự từ bàn phím
    3. Tìm và in ra tất cả các vị trí của ký tự vừa nhập trong chuỗi đã nhập"""
s=input("Nhập chuỗi kí tự: ")
s_1=input("Nhập kí tự: ")
for i in range(len(s)):
    if s[i] == s_1: print(i)