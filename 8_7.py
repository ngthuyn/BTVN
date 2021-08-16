"""Bài 08:  chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không."""
a=(1,1,1,1,1)
dem=0
for i in range(len(a)):
    if a[0]==a[i]: dem+=1
print("Tất cả các phần tử trong tuple giống nhau") if dem==len(a) else print(f"Có {dem} phần tử trong tuple giống nhau")