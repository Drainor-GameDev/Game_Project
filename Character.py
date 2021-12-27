from Item import *
class Guerrier:

    def __init__(self, name="Vol'jin",level=1,armor=20,dodge=3.5,parry=25.5,critProbability=2.3,critDamage=55,chestPlate=Chest(),weapon=Weapon()):
        self.name = name
        self.initiative = 12
        self.dmg = 7
        self.pv = 120
        self.level = level
        self.armor = armor
        self.dodge = dodge
        self.parry = parry
        self.critProbability = critProbability
        self.critDamage = critDamage
        self.chestPlate = chestPlate
        self.weapon = weapon

    def get_name(self):
        return self.name

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

    def get_chestPlate(self):
        return self.chestPlate

    def get_weapon(self):
        return self.weapon

    def __str__(self):
        return f"{self.name} le Barbare ({self.pv} PV)"

    def decrement_PV(self, damage):
        self.pv -= damage

