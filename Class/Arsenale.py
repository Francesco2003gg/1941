from Class.Arma import Weapon

class Arsenal:
  """
  Classe per la creazione dell'arsenale contenente le armi.
  """
  
  def __init__(self) -> None:
    """
    Inizializza la flotta di armi.
    """
    self.weapons = [] # Lista delle armi
    
  def add_weapon(self, weapon:Weapon) -> None:
    """
    Aggiunge un'arma all'arsenale.
    
    weapon: l'arma da aggiungere
    """
    self.weapons.append(weapon)
    
  def remove_weapon(self, weapon:Weapon) -> None:
    """
    Rimuove un'arma dall'arsenale.
    
    weapon: l'arma da rimuovere
    """
    self.weapons.remove(weapon)
    
  def total_power(self) -> int:
    """
    Restituisce la dimensione dell'arsenale.
    
    return:
    - total_power: la dimensione dell'arsenale
    """
    return sum([w.get_power() for w in self.weapons])
  
  def still_usable(self) -> list:
    """
    Restituisce il numero di armi ancora utilizzabili.
    """
    return ([w for w in self.weapons if not w.used])
  
  def empty(self) -> bool:
    """
    Restituisce True se le armi sono state tutte utilizzate, False altrimenti.
    """
    return True if len(self.still_usable()) == 0 else False
  
  #aggiungiamo i metodi per scorrere le armi
  def __iter__(self):
    """
    Restituisce un iteratore sull'arsenale.
    """
    return iter(self.weapons)
  
  def __getitem__(self, index):
    """
    Restituisce l'arma in posizione index.
    """
    return self.weapons[index]