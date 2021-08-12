"""Bài 05. Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list. Nếu có nhiều phần tử
có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng."""
def max_count(list):
    list1=[]
    for i in range(len(list)):
        list1.append(list.count(list[i]))
    print(list1)
    for i in range(len(list)):
        if max(list1)==list.count(list[i]):
            print(list[i])
            break
max_count([1,2,1,1,3,4,1,1,8,2,4,6,8,9,8,8,8])