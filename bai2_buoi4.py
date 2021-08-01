"""Bài 02. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím"""
import math
n =int(input("Nhập số  nguyên dương: "))
x =float(input("Nhập số thực : "))
s_1=s_2=s_3=a=1
for i in range(1,n+1):

    s_1+=math.pow(x,i)
    s_2+=math.pow(-1,i)*math.pow(x,i)
    a=a*i
    s_3+=math.pow(x,i)/a
print(s_1)
print(s_2)
print(s_3)

