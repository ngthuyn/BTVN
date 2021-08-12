"""Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list)"""
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2= [[3,2,1],[6,5,4],[9,8,7]]
cot=[]
t=0
for i in range(0,3):
    for row in matrix2: # trích cột:
        cot.append(row[i])
    for j in range(0,3):
        t+=matrix1[i][j]*cot[j]
    cot.clear()
print(f"Tích của 2 ma trận là: {t}")