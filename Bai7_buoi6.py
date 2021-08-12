"""
Viết chương trình kiểm tra xem 2 list có phần tử chung không
"""
def kiemtra(list1,list2):
    dem=0
    for i in range(len(list1)):
        if list1[i] in list2: dem+=1
    print(f"2 list có phần tử chung và số phần tử chung là {dem}") if dem >=1 else print("2 list không có phần tử chung")
kiemtra(['apple','banana','cherry',"orange", "kiwi", "melon", "mango"],[1,2,3,4,5, "melon", "mango"])