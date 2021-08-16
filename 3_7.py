"""Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple."""
def ktra(tuple):
    dem=0
    a=()# tạo tuple rỗng
    for i in range(len(tuple)):
        if type(tuple[i])!= type(a):
            dem += 1
        else: break
    print(dem)
ktra([1,2,3,(1,2)])

