from menu import menu
class Restaurent:
    def __init__(self,name) -> None:
        self.name=name
        self.employee_list=[]
        self.menu=menu()
    
    def add_employee(self,emplo):
      
        self.employee_list.append(emplo)
        print(f"{emplo.name} is added to the employee List")


    def view_employee(self):
        print("Here is your employee List:\n")
        for i in self.employee_list:
            print(i.name, i.phone, i.email, i.address,i.designation)


      