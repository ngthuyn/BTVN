"""Bài 05. Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str"""
def count_upper_lower(str1):
    h=k=0
    for i in str1:
        if 97 <= ord(i) <= 122: k+=1

        if 65 <= ord(i) <= 90: h+=1
        """Cách khác:
        if i.isupper(): h+=1
        if i.islower():k+=1"""
    print(f"Trong chuỗi có {h} chữ viết hoa ")
    print(f"Trong chuỗi có {k} chữ viết thường ")
count_upper_lower("DadsdFGHJKghj")
