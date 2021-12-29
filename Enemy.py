from random import randint

class Boss:

    def __init__(self, name="Illidan",level="??",armor=50,dodge=3,parry=30,critProbability=1,critDamage=1005):
        self.name = name
        self.initiative = 12
        self.dmg = 10000
        self.pv = 1000000
        self.level = level
        self.armor = armor
        self.dodge = dodge
        self.parry = parry
        self.critProbability = critProbability
        self.critDamage = critDamage

    def get_name(self):
        return self.name
    
    def get_class(self):
        return "Guerrier"

    def get_initiative(self):
        return self.initiative

    def get_dmg(self):
        return self.dmg

    def get_pv(self):
        return self.pv

    def get_level(self):
        return self.level

    def get_armor(self):
        return self.armor

    def get_dodge(self):
        return self.dodge

    def get_parry(self):
        return self.parry

    def get_critProbability(self):
        return self.critProbability

    def get_critDamage(self):
        return self.critDamage

    def __str__(self):
        return self.name

    def decrement_PV(self, damage):
        if randint(0,100) <= self.dodge:
            print("Esquivé")
        elif randint(0,100) <= self.parry:
            print("Parré")
        else:
           self.pv -= int(damage*(self.armor / 100))