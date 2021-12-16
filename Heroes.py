class Barbare:

    def __init__(self, name="Conan", initiative=12, dmg=7, pv=120):
        self.name = name
        self.initiative = initiative
        self.dmg = dmg
        self.pv = pv

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


combatant = Barbare("YANIS")

print(combatant)
