create_food_num = 0


class Item:
    def __init__(self, name, description, list_of_ing, price):
        global create_food_num
        create_food_num += 1
        self.item_id = create_food_num
        self.name = name
        self.description = description
        self.list_of_ing = list_of_ing
        self.price = price

    
    def __repr__(self):
        return f"Name: {self.name} \nDescription: {self.description}\nList of Ingredients in Meal: {self.list_of_ing}\nPrice: {self.price}\n"

    
class App:
    def __initi__(self, menu_list):
        self.menu_list = []

    def create_item(self, name, description, list_of_ing, price):
        new_item = Item(name, description, list_of_ing, price)
        food_id = (create_food_num)
        add_this = (food_id, new_item)
        self.menu_list.append(add_this)
        print(f"Meal#: {create_food_num} \nName: {name} \nDescription: {description}\nList of Ingredients in Meal: {list_of_ing}\nPrice: {price}\n")

    def remove_item(self, delete_item):
        remove_menu = delete_item
        for i in self.menu_list:
            if remove_menu == str(i[0]):
                self.menu_list.remove(i)
                break
        else:
            print("Delete did not work, try again.")
    
    def all_items(self):
        show_all = True
        if show_all:
            return self.menu_list
        else:
            pass

# my_menu = Item("Pizza", "Cheese Pizza", "Dough, Tomato sauce, cheese", 18)
# print(my_menu)

