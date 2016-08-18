class Being():
    def __init__(self, base_line_1, body1, base_line_2, body2, wounds_table, fate_table):
        self.base_line_1 = base_line_1
        self.body1 = body1
        self.base_line_2 = base_line_2
        self.body2 = body2
        self.wounds_table = wounds_table
        self.fate_table = fate_table


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
