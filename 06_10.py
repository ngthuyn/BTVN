"""Bài 06. Xây dựng class User để lưu trữ thông tin người dùng hệ thống
    - Thuộc tính: first_name, last_name, birthday, email, address, username, password
    - Hành vi (phương thức): login(), logout(), update_info()"""

class User:
    def __init__(self,first_name="",last_name="",birthday="",email="",address="",username="",password=""):
        self.first_name=first_name
        self.last_name=last_name
        self.birthday=birthday
        self.email=email
        self.address=address
        self.username=username
        self.password=password
    
    def login(self):
        """self.first_name=input("Nhập first_name: ")
        self.last_name=input("Nhập last_name: ")
        self.birthday=input("Nhập birthday: ")
        self.email=input("Nhập email: ")
        self.address=input("Nhập address: ")"""
        
        self.username=input("Nhập username: ")
        self.password=input("Nhập password: ")


    def logout(self):
      while True:
           choice=int(input("Nhập số 1 để logout(): "))

           if choice==1: 
               print("Bạn đã logout thành công")
               break
           else:
               print("Nhập lại!")
               continue


    def update_infor(self):
        print("--THAY ĐỔI THÔNG TIN CÁ NHÂN--")
        while True:
            choice=int(input("Chọn số từ 1->7: " ))

            if choice==1: 
                self.first_name=input("Nhập thông tin thay đổi: ")
                print(f"first_name: {self.first_name}")
                continue
                
            elif choice==2:
                self.last_name=input("Nhập thông tin thay đổi : ")
                print(f"last_name: {self.last_name}")
                continue  

            elif choice==3:
                self.birthday=input("Nhập thông tin thay đổi : ")
                print(f"birthday: {self.birthday}")
                continue

            elif choice==4:
                self.email=input("Nhập thông tin thay đổi : ")
                print(f"email: {self.email}")
                continue

            elif choice==5:
                self.address=input("Nhập thông tin thay đổi : ")
                print(f"address: {self.address}")
                continue

            elif choice==6:
               self.username=input("Nhập thông tin thay đổi : ")
               print(f"username: {self.username}")
               continue

            elif choice==7:
               self.password=input("Nhập thông tin thay đổi : ")
               print(f"password: {self.password}")
               continue

            elif choice==0: 
                print("Thông tin thay đổi đã được lưu")
                break


do=User()
do.login()
do.update_infor()
do.logout()

