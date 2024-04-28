class menu:  
    def __init__(self) -> None:
        self.menu_list=[]
     
 
    def add_mn_item(self,item):
        self.menu_list.append(item)

    def check_mn_item(self,item):
        for i in self.menu_list:
            if i.name.lower()==item.lower():
                return i
            
        print("this item isnot available")
    
    def remove_mn_item(self,item):
            item=self.check_mn_item(item)
            if item:
             self.menu_list.remove(item)
             print(f"{item.name} is delete from menu")

            else:
                print("item isnot available")

    def show_mn_item(self)->None:
        print("____SHOW MENU_____")
        print("Item name\tprice\tQuantity")
        for i in self.menu_list:
            print(f"{i.name}\t\t{i.price} \t {i.quantity}")

        
