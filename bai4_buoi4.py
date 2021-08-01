"""Bài 04. Lập trình thực hiện các công việc sau:
    1. Nhập 3 số a, b, c bất kì
    2. Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    3. Nếu đúng là tam giác thì xác định là tam giác vuông hay không?"""
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    if a*a==b*b+c*c or a*a+b*b==c*c or b*b==a*a+c*c:
        print(f"{a},{b},{c} là độ dài 3 cạnh trong tam giác vuông")
    else: print(f"{a},{b},{c} là độ dài 3 cạnh trong tam giác . Đây không phải tam giác vuông")
else: print(f"{a},{b},{c} không phải độ dài 3 cạnh trong tam giác.")

