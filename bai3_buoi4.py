"""Bài 03. Lập chương trình thực hiện các công việc sau:
    1. Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    2. Tính tổng các chữ số của số đó.
    3. Hiển thị kết qủa ra màn hình"""
while True:
    n=int(input("Nhập số nguyên dương< 1000: "))
    if n>0 and n<1000: break
    else: print("Nhập lại!")
if n<10: print(f"Tổng={n}")
elif n>10 and n<100: print(f"Tổng={n//10+n%10}")
else: print(f"Tổng={n//100+(n%100)//10+(n%100)%10}")