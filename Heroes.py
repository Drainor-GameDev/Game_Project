class Barbare:

    def __init__(self, name="Conan"):
        self.name = name
        self.initiative = 12
        self.dmg = 7
        self.pv = 120

    def get_name(self):
        return self.name

    def get_initiative(self):
        return self.initiative

    def get_dmg(self):
        return self.dmg

    def get_pv(self):
        return self.pv

    def __str__(self):
        return f"{self.name} le Barbare ({self.pv} PV)"

    def decrement_PV(self, damage):
        self.pv -= damage

