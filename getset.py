class student:
    def __init__(self,name,roll_number,password):
        self.name=name
        self._roll_number=roll_number
        self.__password=password
    def display_details(self):
        print("name:",self.name)
        print("Roll Number:",self._roll_number)
        print("password:",self.__password)
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password=new_password
student=student("Alice","A001","secure_pass")
print("Name (public):",student.name)
print("Roll Number(procted):",student._roll_number)
print("password(private):",student.get_password())
student.set_password("new_welcome")
student.display_details()