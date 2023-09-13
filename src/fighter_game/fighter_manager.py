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
        return name
    
    def create_weapon(self, name, power):
        """
        créé une nouvelle arme
        """
        name = Weapon(name, power)
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
        while fighter1.get_healthpoints() > 0 and fighter2.get_healthpoints() > 0:
            if weapon1.get_ammo() == 0:
                fighter1.punch(fighter2)
            else:
                fighter1.fighter_shoot(fighter2)
            if fighter2.get_healthpoints() < 1:
                weapon2._owner = None
                fighter2._weapon = None
                return fighter1
            if weapon2.get_ammo() == 0:
                fighter2.punch(fighter1)
            else:
                fighter2.fighter_shoot(fighter1)
            if fighter1.get_healthpoints() < 1:
                weapon1._owner = None
                fighter1._weapon = None
                return fighter2
        
        
        
manager = FighterManager()
louis = manager.create_fighter("Louis","")
ethan = manager.create_fighter("Ethan","")
pistolet = manager.create_weapon("Pistolet",4)
bazooka = manager.create_weapon("Bazooka",10)







