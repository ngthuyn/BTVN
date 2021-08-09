"""Bài 06. Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần"""
def is_pangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    j=0
    for i in set(str):
        if i.islower(): j+=1
    print("True") if j==26 else print("False")
is_pangram("aghkabcdefghijklmnopqrstuvwxyz")