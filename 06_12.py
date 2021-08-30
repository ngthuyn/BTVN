"""Bài 06. Viết chương trình thêm một chuỗi nào đó vào cuối file
"""
with open('/Users/Asus/PycharmProjects/pythonCore/f.txt', mode='a', encoding='utf-8') as f:
    f.writelines("\nhello world!")
