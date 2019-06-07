from komodocafe_oop import App

class Menu:
    def __init__(self):
        self.app = App()
        self.menu_list = []
        self.actions = {
            "1": self.add_item,
            "2": self.rm_item,
            "3": self.see_all,
            "4":exit
        }
    
    def options(self):
        print(
        """
    Welcome to Komodo Cafe!\nWhat would you like to do?:\n
        1. Add an item
        2. Delete an item
        3. See all items
        4. Exit program
        """
        )
        
    def run(self):
        while True:
            self.options()
            choice = input("> ")
            action = self.actions.get(choice)
            if action:
                action()
            else:
                print(f"{choice}is not a valid choice")
            
        exit()
    
    def add_item(self):
        name = input("What would you like to add? \n> ")
        description = input("What is the description? \n> ")
        list_of_ing = input("What are the ingredients? \n> ")
        price = input("What is the price? \n> ")
        App.create_item(self, name, description, list_of_ing, price)
        # print(f"{create_menu_item} has been added!")
    
    def rm_item(self):
        remove_menu = input("What meal # would you like to remove?\n> ")
        App.remove_item(self, remove_menu)
        print("Your item has been removed.")
        
    def see_all(self):
        print(self.menu_list)
    

if __name__=="__main__":
    menu = Menu()
    menu.run()
    
