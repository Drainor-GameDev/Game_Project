from random import randint

import Heroes
import Hostiles

class Affrontement:

    def __init__(self, lvl='Easy', nb_fight=0, nb_shot=0):
        self._lvl = lvl
        self._nb_fight = nb_fight
        self._nb_shot = nb_shot

    def get_lvl(self):
        return self._lvl

    def get_nb_fight(self):
        return self._nb_fight

    def get_nb_shot(self):
        return self._nb_shot

    def incr_nbCombat(self):
        self._nb_fight += 1

    def incr_nbCoupEchange(self):
        self._nb_shot += 1

    def combatAMort(self, heros, mechant):

        win = ''
        HerosTurn = heros.initiative >= mechant.initiative

        print("Combat opposant ", heros, " à ", mechant)

        while heros.pv > 0 and mechant.pv > 0:
            if HerosTurn:
                mechant.decrement_PV(randint(1, heros.dmg))
                self.incr_nbCoupEchange()
            else:
                heros.decrement_PV(randint(1, mechant.max_dmg))
            print('PAF')
            HerosTurn = not HerosTurn
        print('Arghhhhh....')
        self.incr_nbCombat()
        if heros.pv <= 0:
            print(f"Le monstre ({mechant.pv} PV) a remporté le combat à mort")
        else:
            print(f"{heros.name} le Barbare ({heros.pv} PV), a remporté le combat à mort")


    def survival(self, name):

        heros = Heroes.Barbare(name)
        while heros.pv > 0:
            mechant = Hostiles.Monstre()
            self.combatAMort(heros, mechant)
            print()

        print(f"Avant de mourrir, {heros.name} a remporté ", self.get_nb_fight(),
        " combats dans une lutte durant laquelle se sont échangés ", self.get_nb_shot(), " coups...")





combattant = Heroes.Barbare("Rendal")
gnome = Hostiles.Monstre()
tournoi = Affrontement()
tournoi.survival('YANIS')

