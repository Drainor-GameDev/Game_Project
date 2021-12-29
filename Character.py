from Item import *
from random import randint

class Guerrier:

    def __init__(self, name="Vol'jin",armor=35,dodge=2,parry=25,critProbability=10,critDamage=1005,chestPlate=Chest(),weapon=Weapon()):
        self.name = name
        self.initiative = 12
        self.dmg = 100000
        self.pv = 450000
        self.armor = armor
        self.dodge = dodge
        self.parry = parry
        self.critProbability = critProbability
        self.critDamage = critDamage
        self.chestPlate = chestPlate
        self.weapon = weapon

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

    def get_chestPlate(self):
        return self.chestPlate

    def get_weapon(self):
        return self.weapon

    def __str__(self):
        return f"{self.name} Guerrier ({self.pv} PV) avec {self.weapon} et {self.chestPlate}"

    def decrement_PV(self, damage):
        if randint(0,100) <= self.dodge:
            print("Esquivé")
        elif randint(0,100) <= self.parry:
            print("Parré")
        else:
           self.pv -= int(damage * ((self.armor + self.chestPlate.get_armor) / 100))


print(Guerrier())