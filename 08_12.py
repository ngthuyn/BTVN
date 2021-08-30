"""
Bài 08: Viết hàm def get_size(file): lấy và trả về dung lượng file

"""
def get_size(file):
    f= open(file, mode='r', encoding='utf-8')
    lines=0
    Content = f.read()
    List = Content.split("\n")
  
    for i in List:
        if i:
            lines += 1
    return lines

size=get_size('/Users/Asus/PycharmProjects/pythonCore/f.txt')
print(size)