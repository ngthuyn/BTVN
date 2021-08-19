"""Bài 02. Viết chương trình tìm ra 3 phần tử của dict có key lớn nhất"""
my_dict={
    "ngay":18,
    "thang":8,
    "nam":2021,
    "bai":9,
    "khoa hoc":"pythoncore"
}
a=sorted(my_dict.keys(),reverse=1)
for key in range(3):
    print(f"key: {a[key]}, value: {my_dict[a[key]]}")