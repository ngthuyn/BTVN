"""	Bài 05. Viết chương trình tạo dict mới
 bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước"""
my_dict1={
    "apple":2, "banana":3, "cherry":4, "kiwi":5, "mango":6,"orange":7

}
my_dict2 = {}.fromkeys(my_dict1.keys(),1)

print(my_dict2)

