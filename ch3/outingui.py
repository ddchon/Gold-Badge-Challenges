from komodoouting_oop import OutingApp

class Menu:
    def __init__(self):
            self.app = OutingApp()
            self.actions = {
            "1": self.display_list,
            "2": self.add_outing,
            "3": self.cost_calc,
            "4": exit
        }

    def options(self):
        print(
        """
Welcome to the Komodo Outing App!\nWhat would you like to do?:\n
    1. Display a list of all Outings
    2. Add Individual Outing to a list
    3. Calculations
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
                print(f"{choice}is not a valid choice")
    
        exit()
    
    def display_list(self):
        outing_list = self.app.list_all_outing()
        for i in outing_list:
            print(i)

    def add_outing(self):
        event_type = input("What is your event type? (Golf, Bowling, Amusement Park, Concert): ")
        num_people = int(input("How many people attended? "))
        event_date = input("When was your event date? ")
        cost_person = float(input("What was the cost per person? $ "))
        total_cost = float(input("What was your total cost? $ "))
        new_outing = self.app.add_outings(event_type, num_people, event_date, cost_person, total_cost)
        print(new_outing)

    def cost_calc(self):
        see_all = input("Do you want total of all events? (Y/N)?").lower()
        if see_all == "y":
            result = self.app.total_calc()
            print(f"The total cost of all events is {result}.")
            return
        by_type = input("What cost by event do you want?\n> ").lower()
        type_result = self.app.calc_by_type(by_type)
        print(f"The {by_type} outing's total cost was {type_result}")
        
        

if __name__ == "__main__":
    app = Menu()
    app.run()