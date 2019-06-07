
from komodoinsurance_oop import BadgeApp

class Menu:
    def __init__(self):
        self.app = BadgeApp()
        self.actions = {
            "1": self.add_badge,
            "2": self.badge_update,
            "3": self.list_badges,
            "4": exit}

    def options(self):
        print(
        """
Welcome to the Komodo Badging System!\nWhat would you like to do?\n
    1. Add a Badge
    2. Badge Update
    3. List all badges
    4. Exit
        """)
    
    def run(self):
        while True:
            self.options()
            choice = input("> ")
            action = self.actions.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")
        
        exit()
    
    def add_badge(self):
        b_id = input("Please enter badge ID:\n> ")
        if b_id:
            add_access = input("Would you like to add doors? (y/n)\n> ")
            if add_access == "n":
                self.options()
            elif add_access == "y":
                doors = input('Door(s):\n> ')
                self.app.add_badge_ID_door(b_id, doors)

    def badge_update(self):
        id_update = input("What is the badge number to update?\n> ")
        list_of_doors = input("Remove or Add a door?\n> ").lower()
        if list_of_doors == "remove":
            remove_door = input("What would you like to remove?\n> ")
            self.app.update_badge_remove(list_of_doors, remove_door)
        elif list_of_doors == "add":
            add_choice = input("What door would you like to add?\n> ")
            self.app.update_badge_add(id_update, add_choice)

    def list_badges(self):
        for k, v in self.app.badge_door_dict.items():
            print(f"Badge ID:{k} | Door(s): {v}")

if __name__ == "__main__":
    app = Menu()
    app.run()