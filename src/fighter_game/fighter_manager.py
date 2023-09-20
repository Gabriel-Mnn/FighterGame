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
        
        
        
    def start_fight(self, combattant, combattu):
        """
        automatise le combat et retourne le vainqueur
        """
        if combattant.get_weapon().get_ammo() > 0:
            combattant.fighter_shoot(combattu)
        else:
            combattant.punch(combattu)
        if combattu.get_healthpoints() > 0:
            return self.start_fight(combattu,combattant)
        else:
            combattu.get_weapon()._owner = None
            combattu._weapon = None
            self._fighters.remove(combattu)
            return combattant
            
            
           
           
manager = FighterManager()
louis = manager.create_fighter("Louis","")
ethan = manager.create_fighter("Ethan","")
pistolet = manager.create_weapon("Pistolet",4)
bazooka = manager.create_weapon("Bazooka",10)

louis.take_weapon(bazooka)
ethan.take_weapon(pistolet)





