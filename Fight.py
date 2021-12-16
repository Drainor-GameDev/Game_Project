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
        print(f"Combat opposant {heros.name} le Barbare ({heros.pv} PV) à un monstre armé d'un couteau avec une initiative de {mechant.initiative}")

        while heros.pv > 0 or mechant.pv > 0:

            if heros.initiative > mechant.initiative:
                mechant.decrementPV(randint(1, heros.dmg))
            else:
                heros.decrementPV(randint(1, mechant.dmg))

        if heros.pv <= 0:
            win = mechant.name
        elif mechant.pv <= 0:
            win = heros.name

