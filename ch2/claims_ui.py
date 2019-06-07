from komodoclaims_oop import ClaimApp

class Menu:
    def __init__(self):
        self.app = ClaimApp()
        self.actions = {
            "1": self.see_all,
            "2": self.work_on_claim,
            "3": self.create_new_claim,
            "4": exit
        }

    def options(self):
        print(
        """
    Welcome to Komodo Claims!\nWhat would you like to do?:\n
        1. See all claims
        2. Take care of next claim
        3. Enter a new claim
        4. Exit
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
    
    def see_all(self):
        print("ClaimID    Type        Description        Amount   DateofAccident      DateofClaim     Is it Valid")
        ClaimApp.see_all_claims(self)

    def work_on_claim(self):
        new_work = ClaimApp.take_care_claim(self)
        print(new_work)

    def create_new_claim(self):
        claim_id_num = input("What claim ID would you like to add?\n> ")
        type_of_claim = input("What type of claim is it? Car, Home or Theft\n> ").lower()
        dscrb = input("Enter a claim description:\n> ").lower()
        amt_claim = input("Amount of Damage:\n> ")
        date_of_accident = input("Date of Accident:\n> ")
        date_of_claim = input("Date of Claim:\n> ")   
        is_it_valid = input("Is the date of claim before or 30 days after accident? (T/F)").lower()
        print(ClaimApp.new_claim(self, claim_id_num, type_of_claim, dscrb, amt_claim, date_of_accident, date_of_claim, is_it_valid))
        
        

if __name__ =="__main__":
    menu = Menu()
    menu.run()