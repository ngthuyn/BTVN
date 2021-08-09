"""Bài 01. Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào"""
def timkiem(*numbers):
    global result1, result2
    result1 = min(*numbers)
    result2=max(*numbers)
    return result1,result2
timkiem(1,2,3,4,5,0,-5,-4,-3,-2,-1)
print(result1)
print(result2)