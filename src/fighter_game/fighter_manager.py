"""
An implementation of a fighter module
"""
from fighter import Fighter, Weapon
from my_queue import Queue


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
        if not combattant.get_weapon() == None:
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
    
    def start_tournament(self, n):
        """
        automatise un tournoi et renvoie le vainqueur
        """
        file = Queue()
        for number in range (n):
            self.create_fighter(str(number),'')
        for fighter in (self._fighters):
            file.enqueue(fighter)
        while file.size() > 1:
            vainqueur = self.start_fight(file.dequeue(),file.dequeue())
            file.enqueue(vainqueur)
        champion = file.dequeue()
        print (f"le champion du tournois est {champion}")
        return champion

           
           
manager = FighterManager()
#louis = manager.create_fighter("Louis","")
#ethan = manager.create_fighter("Ethan","")
#pistolet = manager.create_weapon("Pistolet",4)
#bazooka = manager.create_weapon("Bazooka",10)

#louis.take_weapon(bazooka)
#ethan.take_weapon(pistolet)



v = manager.start_tournament(4)

