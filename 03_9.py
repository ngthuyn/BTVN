"""Bài 03. Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử. 
Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict"""
my_dict = {i: [i,i+1,i+2,i+3,i+4,i+5] for i in range(5)}
print(my_dict)
for key in my_dict.keys():
    print(f"Phần tử thứ 5 của Value[{key}]: {my_dict[key][4]}")