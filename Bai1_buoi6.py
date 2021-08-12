"""Bài 01. Viết chương trình tính tổng, tích của các phần tử trong một list."""
def tong_tich(list):
    sum=0
    tich=1
    for i in range(len(list)):
        sum+=list[i]
        tich*=list[i]
    print(sum)
    print(tich)
tong_tich([5,10,15])