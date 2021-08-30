"""
Bài 08: Viết hàm def get_size(file): lấy và trả về dung lượng file

"""
import os
def get_size(file):
    print(os.stat(file).st_size)
   

get_size('/Users/Asus/PycharmProjects/pythonCore/A.txt')
