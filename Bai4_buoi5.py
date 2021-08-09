"""Bài 04. Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False"""
import  math
def is_prime(n):
    k=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: k+=1
    print("True") if k==0 else print("False")
is_prime(123)