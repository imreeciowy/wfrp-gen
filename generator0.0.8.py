class Being():
    def __init__(self, base_line_1, body1, base_line_2, body2):
    # def __init__(self, race, name, current_career, previous_careers, age, gender, secondary_presonal_details, base_line_1, base_line_2, trappings, weapon, armour, skills, talents, money, spells):
        # self.race = race
        # self.name = name
        # self.current_career = current_career
        # self.previous_careers = previous_careers
        # self.age = age
        # self.gender = gender
        # self.secondary_presonal_details = secondary_presonal_details
        self.base_line_1 = base_line_1
        self.body1 = body1
        self.base_line_2 = base_line_2
        self.body2 = body2
        # self.trappings = trappings
        # self.weapon = weapon
        # self.armour = armour
        # self.skills = skills
        # self.talents = talents
        # self.money = money
        # self.spells = spells
              
class Human(Being):
    def __init__(self):
        self.base_line_1 = [20] * 8
        self.body1 = []
        self.base_line_2 = [0] * 8
        self.base_line_2[0] = 1
        self.body2 = []

class Dwarf(Being):
    def __init__(self):
        self.base_line_1 = [30, 20, 20, 30, 10, 20, 20, 10]
        self.body1 = []
        self.base_line_2 = [0] * 8
        self.base_line_2[0] = 1
        self.body2 = []

class Elf(Being):
    def __init__(self):
        self.base_line_1 = [20, 30, 20, 20, 30, 20, 20, 20]
        self.body1 = []
        self.base_line_2 = [0] * 8
        self.base_line_2[0] = 1
        self.body2 = []

class Halfling(Being):
    def __init__(self):
        self.base_line_1 = [10, 30, 10, 10, 30, 20, 20, 30]
        self.body1 = []
        self.base_line_2 = [0] * 8
        self.base_line_2[0] = 1
        self.body2 = []
