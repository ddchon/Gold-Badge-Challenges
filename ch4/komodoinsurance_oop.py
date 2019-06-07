
class Badge:
    def __init__(self, badge_ID, list_of_doors):
        self.badge_ID = badge_ID
        self.list_of_doors = list_of_doors

    def __repr__(self):
        return f"Badge ID: {self.badge_ID} | Door(s): {self.list_of_doors}"

class BadgeApp:
    def __init__(self):
        self.badge_door_dict = {}
        self.list_of_doors = []
    
    def add_badge_ID_door(self, b_id, doors):
        self.badge_door_dict.update({b_id:[doors]})

    def update_badge_add(self, badge_ID, list_of_doors):
        self.badge_door_dict[badge_ID].append(list_of_doors)
    
    def update_badge_remove(self, badge_ID, list_of_doors):
        # for i in self.badge_door_dict:
        #     if i.list_of_doors == remove_door:
        self.badge_door_dict[badge_ID].remove(list_of_doors)

    def list_all_badge(self):
        for k, v in self.badge_door_dict.items():
            return k, v


