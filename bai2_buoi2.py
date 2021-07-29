"""Bài 02. Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>"""
import math
x=float(input())
y=float(input())
z=float(input())
f=(x+y+z)/(x**2+y**2+z**2)-abs(x-z*math.cos(y))
print("f=",f)