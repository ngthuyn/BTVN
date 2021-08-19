"Bài 00. Viết chương trình tính tích value của các phần tử trong một dict"
""
my_dict={
    "ngay":18,
    "thang":8,
    "nam":"hi"
}
tich=1
for value in my_dict.values():
    tich*=value
print(tich)
