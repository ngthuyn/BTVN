"""Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"].
Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên."""
a=["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
for i in range(len(a)):
    b=a[i].split(".")
    print(b[-1])