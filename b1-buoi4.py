#Bài 01. Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $
s=input("Nhập chuỗi kí tự: ")
for i in range(len(s)):
   if  s[i]==s[0]:
       b=s[1:].replace(s[i],'$')
s=s[0]+b
print(s)


