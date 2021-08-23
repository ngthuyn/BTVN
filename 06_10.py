"""Bài 06. Xây dựng class User để lưu trữ thông tin người dùng hệ thống
    - Thuộc tính: first_name, last_name, birthday, email, address, username, password
    - Hành vi (phương thức): login(), logout(), update_info()"""

class User:
    def __init__(self,first_name,last_name,birthday,email,address,username,password):
        self.first_name=first_name
        self.last_name=last_name
        self.birthday=birthday
        self.email=email
        self.address=address
        self.username=username
        self.password=password
    
    def login(self):
        return self.first_name,self.last_name,self.birthday,self.email,self.address,self.username,self.password

    
    def logout(self,choice):
      self.choice=choice
      while True:
        if choice==1: 
            print("Bạn đã logout thành công")
            break
        else:
             print("Nhập lại!")
             


    def update_infor(self,choice):
        self.choice=choice
        if choice==1: 
            self.first_name=input("Nhập thông tin thay đổi: ")
            print(self.first_name)
            
        if choice==2:
            self.last_name=input("Nhập thông tin thay đổi : ")
            print(self.last_name)

        if choice==3:
            self.birthday=input("Nhập thông tin thay đổi : ")
            print(self.birthday)

        if choice==4:
            self.email=input("Nhập thông tin thay đổi : ")
            print(self.email)

        if choice==5:
            self.address=input("Nhập thông tin thay đổi : ")
            print(self.address)
        if choice==6:
            self.username=input("Nhập thông tin thay đổi : ")
            print(self.username)
        if choice==7:
            self.password=input("Nhập thông tin thay đổi : ")
            print(self.password)
        
        if choice==0: 
            print("Lưu thay đổi!")
            


do=User('gsfs','fhfd','sjfos','sjfsd','ksjfsl','sksk',123)
#do.login()
do.logout(1)
#do.update_infor(2)
