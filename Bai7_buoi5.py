"""Bài 07. Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h"""
def body_mass_index(m,h):
    BMI=m/(h**2)
    return BMI
def bmi_information(m,h):
    if body_mass_index(m,h)<18.5: print("Người này gầy")
    elif 18.5<=body_mass_index(m,h)<=24.9: print("Người này bình thường")
    elif 25<= body_mass_index(m,h)<=29.9: print("Người này tiền béo phì")
    elif 30<= body_mass_index(m,h)<=34.9: print("Người này béo phì độ I")
    elif 35<=body_mass_index(m,h)<=39.9: print("Người này béo phì độ II")
    else: print("Người này béo phì độ III")
bmi_information(46,1.55)
