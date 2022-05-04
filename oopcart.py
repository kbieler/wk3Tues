#start small! break it down, plan it out
# what are the options?
    #shopping create server
    #what are their attributes? cart dictionary for item and quantity
    #what are the pieces of functionality- add/delete/show/quit
    #what do they act on? - user input
# add functionality piece by piece and test as you go

class ShoppingCart():
    def __init__(self):
        self.cart = {}

    def show_items(self):
        if self.cart == {}:
            print("Your cart is currently empty.")
        else:
            for i in self.cart:
                print(f'You have {self.cart[i]} {i}.')

    def add_items(self):
        item = input("Wht would you like to add? ")
        amount = int(input("How many would you like to add? "))
        if item in self.cart:
            self.cart[item] += amount
        else:
            self.cart[item] = amount

    def delete_item(self):
        item = input("What would you like to delete?")
        if item.lower() in self.cart:
            del self.cart[item]
        else:
            print("That item is not in your cart.")



def run_program(self):
    while True:
        action = input("Would you like to add, delete, view or quit?")
        if action.lower() == "view":
            self.show_items()
        elif action.lower() == "add":
            self.add_items()
        elif action.lower() == "delete":
            self.delete_item()
        elif action.lower() == "quit":
            print('Thank you! Goodbye!')
            break
        else:
            print("Invalid input. Please try again.")

my_cart = ShoppingCart()

