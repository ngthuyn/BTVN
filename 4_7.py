"""Bài 04: Cho 1 list chứa các tuple không rỗng. Viết chương trình sắp xếp list đó theo
chiều tăng dần của phần tử cuối trong mỗi tuple."""
def sapxep(list):
    A=[]
    for i in range(len(list)):
        A.append(list[i][-1])
    B=sorted(A)
    C=[]
    for i in range(len(list)):
        for j in range(len(list)):
            if B[i]==list[j][-1] and list[j] not in C:# ktra list[j] not in C để tránh trường hợp in lại nhiều lần
                C.append(list[j])
    print(C)
sapxep([(1,3),(5,6,0),(2,8,6),(1,22,6)])