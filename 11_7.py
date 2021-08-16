"""
Bài 11: Viết phương trình tìm từ dài nhất trong 1 câu nhập từ bàn phím
"""
b=input("Nhập câu:").split(" ")
c=[]
for i in range(len(b)):
    c.append(len(b[i]))
#print(c)
#print(b)
for i in range(len(c)):
    if len(b[i])==max(c):
        print(b[i])
        break
