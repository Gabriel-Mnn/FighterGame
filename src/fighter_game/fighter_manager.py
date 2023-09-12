class FighterManager:
    """
    la classe permettant les combats entre combattant
    """
    
    def create_fighter(name):
        """
        créé un nouveau combattant
        """
        name = Fighter(name,'')
        return name.summary()
    
    def create_weapon(name):
        """
        créé un nouveau combattant
        """
        name = Weapon(name)
        return name.summary()
    
    def start_fight(fighter1, fighter2):
        """
        automatise le combat et retourne le vainqueur
        """
        while fighter1._healthpoints > 0 and fighter2._healthpoints > 0:
            fighter1._shoot(fighter2.get_name())
            fighter2._shoot(fighter1.get_name())
        if fighter1._healthpoints > 0 and fighter2._healthpoints < 0:
            return fighter2.get_name()
        if fighter2._healthpoints > 0 and fighter1._healthpoints < 0:
            return fighter1.get_name()
        else:
            return "draw"
            