"""customer
Employee
Admin

"""
from abc import ABC
from orders import order
class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address


class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart=order()
        


    def view_menu(self,restaurent):
        restaurent.menu.show_mn_item()

    def add_to_cart(self,restaurent,item_name,quantity):
            
             item=restaurent.menu.check_mn_item(item_name)
             if item:
                   if quantity>item.quantity:
                     print("items number is exceeded")
                   else:
                     item.quantity=quantity   #user theke pawwa quantity diye amader quantity replace
                     self.cart.add_item(item)
                 
                     print("item added")

             else:
                print("Your item isn't available right now")

    
    def view_cart(self):
        print("_____Here is your Cart_____")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
                  
        print("total price : ",self.cart.total_price())


    def pay_bill(self):
        print(f"Total {self.cart.total_price()}tk payed successfully")
        self.cart.clear()

class employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary) -> None:
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, phone, email, address)

class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        

    def add_employee(self,restaurent,emplo):
        restaurent.add_employee(emplo)
      

    def view_employee(self,restaurent):
        restaurent.view_employee()
    

    def add_item(self,restaurent,item):
        restaurent.menu.add_mn_item(item)
    

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_mn_item(item)

    def show_item(self,restaurent):
        restaurent.menu.show_mn_item()


    def view_menu(self,restaurent):
        restaurent.menu.show_mn_item()
   
   
    












            
        
        

# itemm=fooditem('Burger',40,16)
# item1=fooditem("pizza",50,10)
# item2=fooditem("hotdog",35,20)
# mn=menu()
# mn.add_mn_item(itemm)
# mn.add_mn_item(item1)
# mn.add_mn_item(item2)
# print(mn.show_mn_item())
# admin=admin('ab',345,654,456)

# mamr_cha=Restaurent("mamar res")
# customer1=customer('rabib',432414436,"rabibjahin@gmail.com","Dhaka")
# admin.add_item(mamr_cha,itemm)
# admin.add_item(mamr_cha,item1)
# admin.add_item(mamr_cha,item2)
# customer1.view_menu(mamr_cha)
# item_name=input("Enter item name : ")
# item_quantity =int(input("Enter input Quantity: "))
# customer1.add_to_cart (mamr_cha,item_name,item_quantity)
# customer1.view_cart()

        


# ad=admin(12,32,32,32)
# ad.add_employee('ab',345,654,456,546,32,6754)   #employee k admin theke add o view koraaa
# ad.view_employee()