"""Bài 13. Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1"""
def find_x(a_list,x):
    dem=0
    for i in range(len(a_list)):
        if x==a_list[i]:
            print(i)
            dem+=1
    if dem==0: print(-1)
find_x(["apple", "banana", 1,"cherry",1,2],1)