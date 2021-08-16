"""Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
Sau đó, unpack các phần tử trong một tuple."""
a="hello"
b=2021
c=True
my_tuple=(a,b,c)
print(my_tuple)
#unpack
(A,B,C)=my_tuple
print(A)
print(B)
print(C)
