from random import randint, random


class Montre:
    _ListeArme = ["couteau", "sabre", "marteau"]

    _PuissanceArme = {"couteau": 3, "sabre": 6, "marteau": 9}

    def __init__(self, arme='thomson', max_dmg=10, initiative=randint(5, 20), pv=6):
        self.arme = arme
        self.max_dmg = max_dmg
        self.initiative = initiative
        self.pv = pv
        self.arme = self._ListeArme[randint(0,2)]
        self.max_dmg = self._PuissanceArme[self.arme]

    def __str__(self):
        return f"Un monstre armé d'un {self.arme} avec une initiative de {self.initiative}"

    def get_arme(self):
        return self.arme

    def get_max_dmg(self):
        return self.max_dmg

    def get_initiative(self):
        return self.initiative

    def get_pv(self):
        return self.pv

    def decrement_PV(self, damage):
        self.pv -= damage


monstre = Montre()

print(monstre)