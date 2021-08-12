"""Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau"""
def demchuoi(list):
    dem=0
    for i in range(len(list)):
        if len(list[i])>=2:
            if list[i][0]==list[i][len(list[i])-1]: dem+=1
    print(dem)
demchuoi(['waww','hâh','b','n','ji','hjio'])