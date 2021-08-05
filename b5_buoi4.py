#Bài 05. Viết chương trình in ra các ký tự số trong chuỗi được nhập từ bàn phím
s=input("Nhập chuỗi kí tự : ")
for i in s:
    if '0'<= i <= '9': print(i)