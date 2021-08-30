"""Bài 10. Viết chương trình tạo ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt"""

import os
a='/Users/Asus/PycharmProjects/pythonCore/'
b=[]
for i in range(65,91):
    b.append(chr(i)+'.txt')
#print(b)

for i in range(26):
    #print(os.path.join(a,b[i]))
    with open(os.path.join(a,b[i]),mode='w',encoding='utf-8') as f:
        pass
