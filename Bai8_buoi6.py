"""Bài 08. Cho list các số nguyên dương A. Xây dựng chương trình đếm số
 lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j."""
def nguyenduong(A):
    dem=0
    for i in range(len(A)):
        for j in range(len(A)):
            if i<j and A[i]>A[j]:
                dem+=1
                print(A[i],end=" ")
                print(A[j])
    print(f"Số tập thỏa mãn là: {dem}")
nguyenduong([1,5,4,9,2,8,3,5])