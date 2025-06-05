from Class.Flotta import Navy
from Class.Arsenale import Arsenal
from Class.Arma import BombaAtomica

class Country:
  """
  Classe per la creazione dei paesi.
  """
  
  def __init__(self, name:str, navy:Navy, arsenal:Arsenal) -> None:
    """
    Inizializza il paese.
    """
    self.name = name
    self.navy = navy
    self.arsenal = arsenal
    
  def get_name(self) -> str:
    """
    Restituisce il nome del paese.
    """
    return self.name
    
  def total_strength(self) -> int:
    """
    Restituisce la forza totale del paese.
    """
    return self.navy.size() + self.arsenal.total_power()
  
  def get_navy(self) -> Navy:
    """
    Restituisce la flotta del paese.
    """
    return self.navy
  
  def get_arsenal(self) -> Arsenal:
    """
    Restituisce l'arsenale del paese.
    """
    return self.arsenal
  
  def arsenal_ai(self) -> Arsenal:
    """
    Restituisce l'arsenale dell'AI.
    """
    Arsenale_tmp = Arsenal()
    for _ in range(10):
        w = BombaAtomica()
        Arsenale_tmp.add_weapon(w)
    self.arsenal = Arsenale_tmp