"""Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm"""
a=[]
def kiemtra(list):
    for i in range(len(list)):
        if list[i] not in a:
            a.append(list[i])
    print(a)
    print(f"Độ dài cần tìm :{len(a)}")
kiemtra([1,2,5,4,1,2,6,4,5,23,5])


