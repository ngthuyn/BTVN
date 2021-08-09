"""Bài 03. Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không."""
def is_perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0: s+=i
    print("True") if s==n else print("False")
is_perfect(6)