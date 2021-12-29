import Character
import Item

class Histoire:

    _ListeDiff = ["Facile", "Normal", "Dificile", "True Warrior"]
    _ListeClasses = ["Guerrier", "Mage", "Chasseur", "Paladin"]

    def __init__(self,dificult = 0,Champion = None):

        self.dificult = dificult
        self.Champion = Champion
    
    def StartNewGame(self):
        print(" █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n █░░║║║╠─║─║─║║║║║╠─░░█\n █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        self.dificult = int(input(f"Bienvenue dans votre pire cauchemar héro quelle dificulté souhaitez vous?\n [0: {self._ListeDiff[0]}, 1: {self._ListeDiff[1]}, 2: {self._ListeDiff[2]} 3: {self._ListeDiff[3]}]"))
        self.Champion = self.CreateCharacter()
        print(f"Ainsi commence le long périple de {self.Champion.get_name()} le {self.Champion.get_class()}")
        self.StartHistory()
    
    def CreateCharacter(self):
        classe = int(input(f"Quelle Classe souhaitez vous?\n [0: {self._ListeClasses[0]}, 1: {self._ListeClasses[1]}, 2: {self._ListeClasses[2]} 3: {self._ListeClasses[3]}]"))
        if classe == 0:
            return Character.Guerrier(str(input("Quel est votre nom?")))
        elif classe == 1:
            return Character.Guerrier(str(input("Quel est votre nom?")))
        elif classe == 2:
            return Character.Guerrier(str(input("Quel est votre nom?")))
        else:
            return Character.Guerrier(str(input("Quel est votre nom?")))

    def StartHistory(self):
        print("Vous arrivez devant le temple noir grouillant de démons vous décidez donc d'y entrer en espérant pouvoir retrouver le frère corompu de la congrégation des elfes.\nDevant vous se tiens désormais Supremus gardien du temple.")
        print("Après votre long affrontement contre le gardien, mère Shahraz ne manque pas de vous attaquer.")
        print("Bravo!!! il ne vous reste plus trop de chemin pour accéder au sommet du temple il ne reste que le conseil Illidari à affronter.")
        print("Tandis que le sang de dame Malande jonche le sol Akama vous rejoin pour l'ultime combat contre Illidan.")
        print("Vos forces nuisent à votre combat vous ne pouvez plus vous battre mais un bruit sourd vous interpèle tandis que Maiev Chantelombre fait son apparition pour vous aider dans votre combat.")
        print("Félicitation vous parvenez à éteindre Illidan !!!!!!")

Histoire().StartNewGame()