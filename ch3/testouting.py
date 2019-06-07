
class OutingApp:
    def __init__(self, event_type, num_people, event_date, cost_person):
        self.event_type = event_type
        self.num_people = num_people
        self.event_date = event_date
        self.cost_person = cost_person
        self.cost_event = 0
        self.totalcost_event = 0
        self.allevent_totalcost = 0
        self.total_cost_all = 0
        self.events_list = []

    def __repr__(self):
        return(f"Event Type: {self.event_type}\nNumber Attended: {self.num_people}\nEvent Date: {self.event_date}\nTotal Cost: {self.cost_event}\nCost Per Person: {self.cost_person}")
    
    def list_all_outing(self):
        return self.events_list
    
    def add_outings(self, event_type, num_people, event_date, cost_person):
        new_outing = OutingApp(event_type, num_people, event_date, cost_person)
        self.events_list.append(new_outing)
        return self.events_list

    def total_calc(self, cost_calc_option, calc_event, totalcost_event, allevent_totalcost, total_cost_all):
        while True:
            if cost_calc_option == "1":
                for total in self.events_list:
                    total += self.allevent_totalcost
                else:
                    break
            
            elif cost_calc_option == "2:":
                if calc_event == "golf":
                    for et in self.events_list:
                        et += self.totalcost_event
                else:
                    break
        

        pass


# event1 = (1000, "golf")
# event2 = (1000, "park")
# event3 = (1500, "golf")

# event_list = [event1, event2, event3]

# total = 0
# for i in event_list:
#     if i[1] == "golf":
#         total += i[0]

# print(total)


