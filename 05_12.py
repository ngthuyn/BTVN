"""Bài 05. Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng"""

#number of lines in the file

f= open('/Users/Asus/PycharmProjects/pythonCore/f.txt', mode='r', encoding='utf-8')
lines=0
Content = f.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        lines += 1
f.close()

#main
f= open('/Users/Asus/PycharmProjects/pythonCore/f.txt', mode='r', encoding='utf-8')

while True:
    n=int(input("Nhập vào số dòng cần đọc < lines: "))
    if n < lines:
        for i in range(n):
            print(f.readline())

        break
    else:
        continue
   
       
#print(f.readline())
