class Cell:
  """
  Classe per la creazione della cella della griglia di gioco per la Battaglia Navale.
  """
  
  def __init__(self, row:int, column:str, grid) -> None:
    """
    Inizializza la cella.
    """
    self.pos = (row, column)
    self.ship = None
    self.is_hitted = False
    self.grid = grid
    
  def __repr__(self):
    """
    Restituisce una stringa che rappresenta la cella.
    """
    # Se la cella è stata colpita si comporta sempre allo stesso modo
    if self.is_hitted:
      if self.occupied() and self.ship.dead():
        return "☠️"
      elif self.occupied():
        return "💥"
      else:
        return "❌"
    # Altrimenti si comporta in modo diverso a seconda del proprietario
    else:
      if self.grid.ownership() == "Player" and self.occupied():
        return self.ship.get_col()
      else:
        return "🌊"

  
  def get_pos(self) -> tuple:
    """
    Restituisce la posizione della cella.
    """
    return self.pos
  
  
  def set_ship(self, ship):
    """
    Imposta la nave presente nella cella.
    """
    self.ship = ship
  
  
  def get_ship(self):
    """
    Restituisce la nave presente nella cella.
    """
    return self.ship
  
  
  def occupied(self) -> bool:
    """
    Restituisce True se la cella è occupata da una nave, False altrimenti.
    """
    return True if self.ship != None else False
  

  def hitted(self) -> bool:
    """
    Restituisce True se la cella è stata colpita, False altrimenti.
    """
    return self.is_hitted
  
  
  def hittable(self) -> bool:
    """
    Restituisce True se la cella può essere colpita, False altrimenti.
    """
    return not self.hitted()
  
  
  def hit(self) -> bool:
    """
    Colpisce la cella.
    """
    # !!! AGGIUNGERE VERIFIICA ALLARMI !!!
    if self.occupied():
      self.ship.hit() # self.ship.hit(self.is_hitted)
    self.is_hitted = True