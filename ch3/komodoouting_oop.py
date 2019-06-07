
class Outing:
    def __init__(self, event_type, num_people, event_date, cost_person, total_cost):
        self.event_type = event_type
        self.num_people = num_people
        self.event_date = event_date
        self.cost_person = cost_person
        self.total_cost = total_cost

    def __repr__(self):
        return(f"Event Type: {self.event_type}\nNumber Attended: {self.num_people}\nEvent Date: {self.event_date}\nTotal Cost: {self.total_cost}\nCost Per Person: {self.cost_person}")

class OutingApp:
    def __init__(self):
        self.events_list = []
    
    def list_all_outing(self):
        return self.events_list
    
    def add_outings(self, event_type, num_people, event_date, cost_person, total_cost):
        new_outing = Outing(event_type, num_people,event_date, cost_person, total_cost)
        self.events_list.append(new_outing)
        return new_outing

    def total_calc(self):
        total = 0
        for i in self.events_list:
            total += i.total_cost
        return total
    

    def calc_by_type(self, outing_type):
        total = 0
        for i in self.events_list:
            if i.event_type == outing_type:
                total += i.total_cost
        return total
