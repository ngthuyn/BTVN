import math
# phương trình dạng ax^2+bx+c=0
print("Nhập a:")
a=int(input())
print("Nhập b:")
b=int(input())
print("Nhập c:")
c=int(input())

if a==0:
    if b==0 and c==0: print("Phương trình có vô số nghiệm.")
    elif b==0 and c!=0: print("Phương trình vô nghiệm.")
    else: print(f"Phương trình có một nghiệp duy nhất:  x={-c/b}")
else:
    delta=b**2-4*a*c
    if delta > 0:
        print("Phương trình có 2 nghiệm phân biệt:")
        print(f"Nghiệm thứ nhất: x_1={(-b+math.sqrt(delta))/(2*a)}")
        print(f"Nghiệm thứ nhất: x_2={(-b-math.sqrt(delta))/(2*a)}")
    elif delta==0: print(f"Phương trình có nghiệm kép : x= {-b/(2*a)}")
    else: print(f"Phương trình vô nghiệm.")