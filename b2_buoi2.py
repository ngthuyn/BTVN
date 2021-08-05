"""Bài 02. Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong
 chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng"""
s=input("Nhập chuỗi:")
if len(s)<=2: print("Chuỗi rỗng!")

else:
    b=s[0:2]+s[len(s)-2:]
    print(b)