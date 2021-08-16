"""Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không."""
a=(1,2,3,4,5)
b=(1,3,5,7)
dem=0
for i in range(len(a)):
    if a[i] in b: dem+=1
print(f"a và b có {dem} phần tử chung") if dem!=0 else print("a và b không có phần tử chung")