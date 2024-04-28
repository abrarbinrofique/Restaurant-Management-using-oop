class order:
    def __init__(self):
        self.items={}
   
    def add_item(self, item):
        if item in self.items:
            self.items[item] +=item.quantity  # Update quantity
        else:
            self.items[item] =item.quantity #jodi already na thake

    
    def remove_cart(self,del_item):
            if del_item in self.items:
                del  self.items[del_item] #jodi item cart e already thake 
                print(f"{del_item} has removed from your cart")
            else:
                print("this item wasn't exist in your cart!")


    # @property
    def total_price(self):

        return sum(item.price*quantity for item,quantity in self.items.items()) #python sum function
    
    def clear(self):
        self.items={}



