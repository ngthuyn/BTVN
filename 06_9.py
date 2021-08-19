"""Bài 06. Viết chương trình lấy ra top 3 phần tử có value lớn nhất từ dict"""
my_dict={
    "apple":2, "banana":3, "cherry":4,  "mango":6,"orange":7,"kiwi":5
}
a=sorted(my_dict.values(),reverse=1)
for i in range(3):
    for key in my_dict.keys():
        if my_dict[key]==a[i]: print(f"key: {key}, value: {my_dict[key]}")
