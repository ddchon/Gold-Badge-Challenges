
claims_list = []

class Claim:
    def __init__(self, claim_id, claim_type, claim_descrip, claim_amt, claim_dateofincident, claim_dateofclaim, is_valid):
        self.claim_id = claim_id
        self.claim_type = claim_type
        self.claim_descrip = claim_descrip
        self.claim_amt = claim_amt
        self.claim_dateofincident = claim_dateofincident
        self.claim_dateofclaim = claim_dateofclaim
        self.is_valid = is_valid
    
    def __repr__(self):
        return f"{self.claim_id}          {self.claim_type}     {self.claim_descrip}        {self.claim_amt}      {self.claim_dateofincident}         {self.claim_dateofclaim}          {self.is_valid}"

class ClaimApp:
    def __init__(self):
        pass
    
    def see_all_claims(self):
        for i in claims_list:
            print(i)
        
    
    def take_care_claim(self):
        # claims_list[0]
        # f"Here are the details for the next claim to be handled:\nClaimID: {claim_id}\nType: {claim_type}\nDescription: {claim_descrip}\nAmount: {claim_amt}\nDate of Accident: {claim_dateofincident}\nDate of Claim: {claim_dateofclaim}\nIs Valid: {is_valid}"

        print(claims_list[0])
        deal_claim = input("Do you want to deal with this claim now(y/n)? ")
        if deal_claim == "y":
            claims_list.remove(claims_list[0])
            return 'Removed'
        else:
            return 'Not removed'
    
    def new_claim(self, claim_id, claim_type, claim_descrip, claim_amt, claim_dateofincident, claim_dateofclaim, is_valid):
        new_item = Claim(claim_id, claim_type, claim_descrip, claim_amt, claim_dateofincident, claim_dateofclaim, is_valid)
        claims_list.append(new_item)
        return new_item


# my_claims = Claim(1, "Car", "Hit a car", "$2,500", "111", "111", True)
# my_app = ClaimApp()

# print(my_app.see_all_claims)
