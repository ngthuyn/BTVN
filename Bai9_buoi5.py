"""Bài 09. Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)"""
def count_ood(n):

    dem = 0
    while n>0:
        i=n%10
        n //= 10

        if i%2!=0: dem+=1
    print(f"Tổng các số  lẻ của số đã cho là {dem}")
count_ood(12345236)