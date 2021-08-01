"""Bài 05. Lập chương trình thực hiện các công việc sau:
    1. Nhập số epsilon < 1 từ bàn phím
    2. Tính e = 1 + 1/1! + 1/2! + ... + 1/n! quá trình dừng khi 1/n! < epsilon.
    3. Đưa kết quả ra màn hình"""
e=i=a=1
eps=float(input("Nhập vào epsilon dương < 1: "))
while i>0:
    a=a*(i)
    if 1/a < eps: break
    e+=1/a
    i+=1
print(e)


