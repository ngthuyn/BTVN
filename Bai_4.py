"""Bài 04. Hãy viết đoạn chương trình thực hiện các việc sau:
1. Nhập hai số nguyên a và b từ bàn phím
2. Thực hiện phép chia lấy nguyên (//) và chia lấy dư (%) của a cho b
3. In kết quả 2 phép chia ra màn hình
Lưu ý: Khi nhập giá trị để test, cần thực hiện các trường hợp sau và xem kết quả thu được
    - TH1: a > 0, b < 0
    - TH2: a < 0, b > 0
    - TH3: a < 0, b < 0"""
a=int(input())
b=int(input())
print("a//b=",a//b)
print("a%b=",a%b)
"""- TH1: a =5, b < -3: a//b= -2
a%b= -1
    - TH2: a < -5, b > 3: a//b= -2
a%b= 1
    - TH3: a < -5, b <-3: a//b= 1
a%b= -2

"""