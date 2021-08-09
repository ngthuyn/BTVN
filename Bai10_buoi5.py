"""Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy"""

def kdequyfibo(n):
    f3 = 2
    f1=1
    f2= 1
    fn = 1
    if (n == 1 or n == 2):
        return 1
    if n==3: return 2
    else:
        for i in range(4,n+1):
            fn = f1 +f2+ f3
            f1 = f2
            f2 = f3
            f3= fn
        return fn
def dequyfibo(n):
    if n ==3:
        return 2
    if n == 2 or n==1:
        return 1
    else:
        return dequyfibo(n-1)+dequyfibo(n-2)+dequyfibo(n-3)
n = int(input("Nhập n = "))
print(f"Số Tribonacci thứ {n}  dùng đê quy là {dequyfibo(n)}")
print(f"Số Tribonacci thứ {n}  không dùng đệ quy là {kdequyfibo(n)}")

