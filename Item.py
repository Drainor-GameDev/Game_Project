class Chest:

    def __init__(self, name="Armure Du Roi Déchu", armor = 20,critProbBonus = 10, critDmgBonus = 105,initiativeBonus = 2):
        self.name = name
        self.armor = armor
        self.critProbBonus = critProbBonus
        self.critDmgBonus = critDmgBonus
        self.initiativeBonus = initiativeBonus

    def get_name(self):
        return self.name
        
    def get_armor(self):
        return self.armor
        
    def get_critProbBonus(self):
        return self.critProbBonus
    
    def get_critDmgBonus(self):
        return self.critDmgBonus

    def get_initiativeBonus(self):
        return self.initiativeBonus

    def __str__(self):
        return f"{self.name} ({self.armor} Armure, {self.critProbBonus} Probabilité Critique Bonus, {self.critDmgBonus} Dégats Critiques Bonus, {self.initiativeBonus} Initiative Bonus)"

class Weapon:

    def __init__(self, name="DeuilleGivre", damage = 150000,critProbBonus = 10, critDmgBonus = 1000,initiativeBonus = 10):
        self.name = name
        self.damage = damage
        self.critProbBonus = critProbBonus
        self.critDmgBonus = critDmgBonus
        self.initiativeBonus = initiativeBonus

    def get_name(self):
        return self.name
        
    def get_damage(self):
        return self.damage
        
    def get_critProbBonus(self):
        return self.critProbBonus
    
    def get_critDmgBonus(self):
        return self.critDmgBonus

    def get_initiativeBonus(self):
        return self.initiativeBonus

    def __str__(self):
        return f"{self.name} ({self.damage} Dégats, {self.critProbBonus} Probabilité Critique Bonus, {self.critDmgBonus} Dégats Critiques Bonus, {self.initiativeBonus} Initiative Bonus)"

