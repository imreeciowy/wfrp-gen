class Being():
    def __init__(self, base_line_1):
    #def __init__(self, race, name, current_career, previous_careers, age, gender, secondary_presonal_details, base_line_1, base_line_2, trappings, weapon, armour, skills, talents, money, spells):
        #self.race = race
        #self.name = name
        #self.current_career = current_career
        #self.previous_careers = previous_careers
        #self.age = age
        #self.gender = gender
        #self.secondary_presonal_details = secondary_presonal_details
        self.base_line_1 = base_line_1
        #self.base_line_2 = base_line_2
        #self.trappings = trappings
        #self.weapon = weapon
        #self.armour = armour
        #self.skills = skills
        #self.talents = talents
        #self.money = money
        #self.spells = spells
        
        
# having human as a base being is tempting, but it is not very developmental
class Human(Being):
    base_line_1 = [20] * 8
        

class Dwarf(Being):
    pass
    
    
class Elf(Being):
    pass
    
    
class Halfling(Being):
    pass
