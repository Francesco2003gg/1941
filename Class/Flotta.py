from Class.Nave import Ship
class Navy:
  """
  Classe per la creazione della flotta di navi.
  """
  
  def __init__(self):
    """
    Inizializza la flotta di navi.
    """
    self.ships = [] # Lista delle navi
    
  def add_ship(self, ship:Ship) -> None:
    """
    Aggiunge una nave alla flotta.
    """
    self.ships.append(ship)
    
  def remove_ship(self, ship:Ship) -> None:
    """
    Rimuove una nave dalla flotta.
    
    ship: la nave da rimuovere
    """
    self.ships.remove(ship)
    
  def size(self):
    """
    Restituisce la dimensione della flotta, cioè la somma delle dimensioni delle navi.
    """
    return sum([ship.dim() for ship in self.ships])
  
  def still_alive(self):
    """
    Restituisce il numero di navi ancora vive nella flotta.
    """
    return len([ship for ship in self.ships if not ship.dead()])
  
  def end(self) -> bool:
    """
    Restituisce True se la flotta è stata distrutta, False altrimenti.
    """
    return self.still_alive() == 0
    
  #aggiungiamo i metodi per scorrere le navi
  def __iter__(self):
    """
    Restituisce un iteratore sulla flotta di navi.
    """
    return iter(self.ships)
  
  def __getitem__(self, index):
    """
    Restituisce la nave in posizione index.
    """
    return self.ships[index]