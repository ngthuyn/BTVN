"""Bài 04. Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict"""
my_dict1={
    "apple":2, "banana":3, "cherry":4, "kiwi":5, "mango":6,"orange":7

}
my_dict2={
    "apple":2, "banana":3, "cherry":4,"orange":5,"water melon":6
}
for item in my_dict1.items():
    if item in my_dict2.items(): print(item)