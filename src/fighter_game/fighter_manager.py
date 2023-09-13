from fighter_game.fighter import Fighter, Weapon



class FighterManager:
    """
    la classe permettant les combats entre combattant
    """
    def __init__(self):
        self._fighters = []
        self._weapons = []
    
    def create_fighter(self, name, description):
        """
        créé un nouveau combattant
        """
        name = Fighter(name, description)
        self._fighters.append(name)
        return name
    
    def create_weapon(self, name, power):
        """
        créé une nouvelle arme
        """
        name = Weapon(name, power)
        self._weapons.append(name)
        return name
    
    def _fight(combattant,combattu):
        """
        le combattant tire ou frappe
        """
        pass
    
    def start_fight(self, fighter1, weapon1, fighter2, weapon2):
        """
        automatise le combat et retourne le vainqueur
        """
        fighter1.take_weapon(weapon1)
        fighter2.take_weapon(weapon2)
        combattant = fighter1
        combattu = fighter2
        while combattant.get_healthpoints() > 0 and combattu.get_healthpoints() > 0:
            if combattant.get_weapon().get_ammo() == 0:
                combattant.punch(combattu)
            else:
                combattant.fighter_shoot(combattu)
            if combattu.get_healthpoints() < 1:
                combattu.get_weapon()._owner = None
                combattu._weapon = None
                self._fighters.remove(combattu)
                return combattant
            combattant, combattu = combattu , combattant #inversion des roles
        
manager = FighterManager()
louis = manager.create_fighter("Louis","")
ethan = manager.create_fighter("Ethan","")
pistolet = manager.create_weapon("Pistolet",4)
bazooka = manager.create_weapon("Bazooka",10)







