"""Bài 05. Viết một class NewString trong đó có 2 phương thức: get_string() và print_string()
    - get_string - nhận một string do người dùng nhập vào
    - print_string - in string nhập vào ở dạng toàn chữ in hoa"""

class NewString:
    def __init__(self,str=input()):
        self.str=str
    
    def get_string(self):
        return self.str

    def print_string(self):
        print(f"string ở dạng in hoa là {self.str.upper()}")
do=NewString()
do.get_string()
do.print_string()