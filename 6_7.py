"""Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple."""
a=(1,2,3,4,5)
if len(a)>=4:
    print(f"2 phần tử thỏa mãn yêu cầu đề bài :{a[3]} và {a[-4]}")
else: print(" không in được do kích thước tuple <4")
