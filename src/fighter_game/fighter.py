from random import randrange, uniform

class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._agility = randrange(1,9)
        self._healthpoints = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self._weapon = None
        
    def get_name(self):
        """
        Retourne le nom du combattant.
        """
        return self._name
    
    def get_description(self):
        """
        Retourne la description du combattant.
        """
        return self._description
    
    def set_description(self, description):
        """
        Affecte la description du combattant.
        
        """
        self._description=description
        
    def get_agility(self):
        """
        retourne l'agilité du combattant
        """
        return self._agility
        
    def get_healthpoints(self):
        """
        retourne les points de vie du combattants
        """
        return self._healthpoints
    
    def get_strength(self):
        """
        retourne la force du combattant
        """
        return 10-self._agility
    
    def get_weapon(self):
        """
        retourne l'arme équipé par le combattant
        """
        return self._weapon
    
    def set_weapon(self, a_weapon):
        """
        donne une arme au combattant
        """
        self._weapon = a_weapon
    
    def take_weapon(self, weapon):
        """
        donne une arme au  combattant
        """
        if weapon._owner == None:
            self.set_weapon(weapon)
            weapon.set_owner(self)
            return self.get_weapon()
        else:
            return None
    
    def fighter_shoot(self,fighter):
        """
        le combattant utilise son arme pour tirer sur un autre combattant
        """
        return self.get_weapon().shoot(fighter)
        
    
    def punch(self, fighter):
        """
        un combattant enlève des pv à un autre combattant
        """
        points=int(uniform(0.7,1.0)*10*self.get_strength()/fighter.get_agility())
        fighter._healthpoints -= points
        print (fighter._healthpoints)
    
    def summary(self):
        """
        retourne une description du combattant
        """
        resume = "nom: " + self.get_name() + "\n"
        resume += "description: " + self.get_description()+ "\n"
        resume += "point de vie: " + self.get_healthpoints()+ "\n"
        resume += "agilité: " + self.get_agility()+ "\n"
        resume += "force: " + self.get_strength()+ "\n"
        return resume

class Weapon:
    """
    La classe d'une arme
    """
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage
        self._ammo = 15-self._damage
        self._owner = None
        
    def get_name(self):
        """
        Retourne le nom de l'arme.
        """
        return self._name
    
    def get_damage(self):
        """
        retourne la puissance de l'arme
        """
        return self._damage
    
    def get_ammo(self):
        """
        retourne le nombre de munition de l'arme
        """
        return self._ammo
    
    def summary(self):
        """
        retourne une description du combattant
        """
        resume = "nom: " + self.get_name() + "\n"
        resume += "degat: " + self.get_damage()+ "\n"
        resume += "force: " + self.get_ammo()+ "\n"
        return resume
    
    def get_owner(self):
        """
        donne le propriétaire de l'arme
        """
        return self._owner
    
    def set_owner(self,a_fighter):
        """
        Donne l'arme au combattant
        """
        self._owner = a_fighter
    
    def shoot(self, fighter):
        """
        un combattant tire sur un autre combattant avec l'arme et lui enlève des pv
        """
        ammo = self.get_ammo()
        if ammo >= 1:
            points = self.get_damage()
            self._ammo -= 1
            fighter._healthpoints -= points
            return points
        elif ammo <= 0:
            return"nothing happened"
    
    
    
pistolet = Weapon('pistolet', 5)    
marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
maurice = Fighter('Maurice', 'The second best one')# on instancie avec les variables de la méthode __init__




