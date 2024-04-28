from fooditem import fooditem
from menu import menu
from orders import order
from Restaurant_management_system import Restaurent
from user import Admin ,employee,Customer

mamar_res=Restaurent("mamar restaurent")
def customer_menu():
 name=input("Enter your name: ")
 email=input("Enter your Email address: ")
 phone=input("Enter your phone number: ")
 address=input("Enter your Address: ")

 customer=Customer(name=name,email=email,phone=phone,address=address)
 while(True):
  print(f"Welcome {customer.name} o_0 ")
  print("1.view menu")
  print("2.Add item to cart")
  print("3.view Cart")
  print("4.pay Bill")
  print("5. EXIT")

  choice=int(input("Enter your choice: "))
  if choice==1:
   customer.view_menu(mamar_res)

  elif choice==2:
   item_name=input("Enter item name : ")
   item_quantity =int(input("Enter input Quantity: "))
   customer.add_to_cart (mamar_res,item_name,item_quantity)


  elif choice==3:
   customer.view_cart()

  elif choice==4:
   customer.pay_bill()
  elif choice==5:
   print(">>> EXIT <<<")
   break
  
  else:
   print("invalid input try again")





def admin_menu():
 name=input("Enter your name: ")
 email=input("Enter your Email address: ")
 phone=input("Enter your phone number: ")
 address=input("Enter your Address: ")
 admin=Admin(name=name,email=email,phone=phone,address=address)
 while(True):
  print(f"Welcome {admin.name} o_0 ")
  print("1.Add new employee")
  print("2.Add new item")
  print("3.view employee")
  print("4.view items")
  print("5.Delete items")
  print("6.EXIT")

  choice=int(input("Enter your choice: "))
  if choice==1:
   name=input("enter employee name: ")
   phone=input("add phone number: ")
   email=input("add email: ")
   designation=input("add job designation: ")
   age=input("Add employere age")
   salary=input("Employee salary: ")
   Address=input("Add employee Address: ")
   empo=employee(name, phone, email, Address,age,designation,salary)
   admin.add_employee(mamar_res,empo )
  elif choice==2:
   item_name=input("Enter item name : ")
   item_price=int(input("Enter item price: "))
   item_quantity =int(input("Enter input Quantity: "))
   ite=fooditem(item_name,item_price,item_quantity)
   admin.add_item (mamar_res,ite)


  elif choice==3:
   admin.view_employee(mamar_res)

  elif choice==4:
   admin.view_menu(mamar_res)
  elif choice==5:
   item=input("enter your item: ")
   admin.remove_item(mamar_res,item)

  elif choice==6:
   print(">>> EXIT <<<")
   break

  
  else:
   print("invalid input try again")


while True:
 print("<<< WELCOME >>>")
 print("1.Customers")
 print("2.Admin")
 print("3.EXIT")
 ch=int(input("Enter Your Choice: "))
 if ch==1:
  customer_menu()
 elif ch==2:
  admin_menu()

 elif ch==3:
  print(">>> EXIT <<<")
  break

 else:
  print("Wrong input try again")
  