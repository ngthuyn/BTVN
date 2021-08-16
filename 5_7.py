"""Bài 05: Viết chương trình tìm ra tuple có phần tử
thứ 2 là nhỏ nhất từ một list chứa các tuple."""
def timkiem(list):
    A=[]
    for i in range(len(list)):
        A.append(list[i][1])
    B=sorted(A)# sắp xếp theo thứ tự tăng dần
    for i in range(len(list)):
        if B[0]==list[i][1]:
            print(list[i])
            break
timkiem([(1,3),(5,0),(2,0,6),(1,22,6)])