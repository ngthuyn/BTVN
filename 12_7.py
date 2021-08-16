"""
Bài 12: Viết phương trình để thử lại các phương thức  của  Set theo danh sách sau

"""
a={1,2,3,4,5,6}
b={1,3,5,7,9}
#
print(set.difference(a,b))
#
print(set.intersection(a,b))
#
print(set.isdisjoint(a,b))
#
print(set.issubset(a,b))
#
print(set.issuperset(a,b))
#
c=set.symmetric_difference_update(a,b)
print('a=',a)
print('b=',b)
print(c)
