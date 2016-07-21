class Being():
    def __init__(self, base_line_1, body1, base_line_2, body2, wounds_table, fate_table):
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
        self.wounds_table = wounds_table
        self.fate_table = fate_table
        # self.trappings = trappings
        # self.weapon = weapon
        # self.armour = armour
        # self.skills = skills
        # self.talents = talents
        # self.money = money
        # self.spells = spells


class Dwarf(Being):
    def __init__(self):
        self.base_line_1 = [30, 20, 20, 30, 10, 20, 20, 10]
        self.body1 = []
        self.base_line_2 = [1, 0, 0, 0, 3, 0, 0, 0]
        self.body2 = []
        self.wounds_table = [11, 12, 13, 14]
        self.fate_table = [1, 2, 3]


class Elf(Being):
    def __init__(self):
        self.base_line_1 = [20, 30, 20, 20, 30, 20, 20, 20]
        self.body1 = []
        self.base_line_2 = [1, 0, 0, 0, 5, 0, 0, 0]
        self.body2 = []
        self.wounds_table = [9, 10, 11, 12]
        self.fate_table = [1, 2, 2]


class Halfling(Being):
    def __init__(self):
        self.base_line_1 = [10, 30, 10, 10, 30, 20, 20, 30]
        self.body1 = []
        self.base_line_2 = [1, 0, 0, 0, 4, 0, 0, 0]
        self.body2 = []
        self.wounds_table = [8, 9, 10, 11]
        self.fate_table = [2, 2, 3]


class Human(Being):
    def __init__(self):
        self.base_line_1 = [20] * 8
        self.body1 = []
        self.base_line_2 = [1, 0, 0, 0, 4, 0, 0, 0]
        self.body2 = []
        self.wounds_table = [10, 11, 12, 13]
        self.fate_table = [2, 3, 3]
