import pandas as pd
from Class.Cell import Cell
from Class.Nave import Ship
from Class.Flotta import Navy

class Grid:
  """
  Classe per la creazione della griglia di gioco per la Battaglia Navale,
   e per l'interazione con quest'ultima.
  """
  
  def __init__(self, n:int, owner:str) -> None:
    """
    Inizializza la griglia di gioco.
    """
    self.owner = owner # "Player" / "AI"
    self.n = n # Dimensione griglia (n x n)
    self.grid = pd.DataFrame(index=range(1, n+1), columns=range(n))
    self.cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"][0 : n]
    self.rows = [i for i in range(1, n+1)]
    
    # Riempiamo il dataframe di celle
    for i in range(n):
      for j in range(n):
        self.grid.iloc[i, j] = Cell(i, self.cols[j], self)
    # Rinomino le colonne
    self.grid.columns = self.cols
    
  
  def dim(self) -> int:
    """
    Restituisce la dimensione della griglia di gioco.
    """
    return self.n
  
  
  def cell(self, riga:int, colonna:str) -> Cell:
    """
    Restituisce la cella specificata della griglia di gioco.
    
    Input:
    - riga: la riga della cella da restituire
    - colonna: la colonna della cella da restituire
    """
    return self.grid.loc[riga, colonna]
  
  
  def xy(self) -> tuple:
    """
    Restituisce le coordinate della griglia di gioco.
    """
    to_return = (self.rows, self.cols)
    return to_return
  
  
  def df(self) -> pd.DataFrame:
    """
    Restituisce il dataframe della griglia di gioco.
    """
    return self.grid
  
  
  def ownership(self) -> str:
    """
    Restituisce il proprietario della griglia di gioco. ("Player" / "AI")
    """
    return self.owner
  
  
  def occupied(self, riga:int, colonna) -> bool:
    """
    Restituisce True se la cella è occupata da una nave, False altrimenti.
    
    Input:
    - riga: la riga della cella da controllare
    - colonna: la colonna della cella da controllare
    """
    if type(colonna) == int:
      colonna = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"][colonna]
    return self.grid.loc[riga, colonna].occupied()
  
  
  def ship_dead(self, riga:int, colonna:str) -> bool:
    """
    Restituisce True se la nave nella cella specificata è affondata, False altrimenti.
    
    Input:
    - riga: la riga della cella da controllare
    - colonna: la colonna della cella da controllare
    """
    ship = self.grid.loc[riga, colonna].get_ship()
    return ship.dead()
  
  
  def check_attack(self, riga:int, colonna:str, type:int = 1) -> bool:
    """
    Controlla se la cella può essere colpita dal tipo di attacco specificato.
    
    Input:
    - riga: la riga della cella da colpire
    - colonna: la colonna della cella da colpire
    - type: il tipo di attacco da effettuare
      I tipi di attacco(type) sono:
        - 1: attacco base
        - 2: bomba atomica, specificare la cella in alto a sinistra
        - 3: radar, specificare la cella centrale

    return:
    - True: se la cella può essere colpita
    - False: se la cella non può essere colpita
    """
    if type == 1:
      return self.grid.loc[riga, colonna].hittable()
    elif type == 2:
      return True if riga != self.rows[-1] and colonna != self.cols[-1] else False
    elif type == 3:
      return True if self.rows[0] < riga < self.rows[-1] and ord(self.cols[0]) < ord(colonna) < ord(self.cols[-1]) else False
    
  
  def hit(self, riga:int, colonna) -> None:
    """
    Colpisce la cella specificata.
    
    Input:
    - riga: la riga della cella da colpire
    - colonna: la colonna della cella da colpire
    """
    if type(colonna) == int:
      colonna = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"][colonna]
    self.grid.loc[riga, colonna].hit()
    
    
  def check_ship_placement(self, ship:Ship, riga:int, colonna:str, direction:int) -> bool:
    """
    Controlla se la nave può essere posizionata nella cella specificata.
    
    Input:
    - ship: la nave da posizionare
    - riga: la riga della cella da posizionare
    - colonna: la colonna della cella da posizionare
    - direction: la direzione della nave (0 = orizzontale, 1 = verticale)
    
    return:
    - True: se la nave può essere posizionata
    - False: se la nave non può essere posizionata
    """
    colonna = self.cols.index(colonna)
    # Se il piazzamento è orizzontale, parte da sinistra
    if direction == 0:
      if colonna + ship.length > self.n:
        return False
      for i in range(ship.length):
        cella = self.grid.loc[riga, self.cols[colonna + i]]
        if cella.occupied() or cella.hitted():
          return False
      return True
    # Se il piazzamento è verticale, parte dall'alto
    elif direction == 1:
      if riga + ship.length > self.n + 1:
        return False
      for i in range(ship.length):
        cella = self.grid.loc[riga + i, self.cols[colonna]]
        if cella.occupied() or cella.hitted():
          return False
      return True
    
  def ship_placement(self, ship:Ship, riga:int, colonna:str, direction:int) -> None:
    """
    Posiziona la nave nella cella specificata.
    Controllo sulla possibilità dio piazzamento già effettuato a priori.
    
    Input:
    - ship: la nave da posizionare
    - riga: la riga della cella da posizionare
    - colonna: la colonna della cella da posizionare
    - direction: la direzione della nave (0 = orizzontale, 1 = verticale)
    """
    colonna = self.cols.index(colonna)
    # Se il piazzamento è orizzontale, parte da sinistra
    if direction == 0:
      for i in range(ship.length):
        self.grid.loc[riga, self.cols[colonna + i]].set_ship(ship)
    # Se il piazzamento è verticale, parte dall'alto
    elif direction == 1:
      for i in range(ship.length):
        self.grid.loc[riga + i, self.cols[colonna]].set_ship(ship)
        
  def possible_positions(self, ship:Ship) -> list:
    """
    Restituisce una lista di tuple contenenti le posizioni possibili per la nave.
    
    Input:
    - ship: la nave da posizionare
    
    return:
    - Una lista di tuple (riga, colonna, direzione) che rappresentano le posizioni possibili
    """
    positions = []
    for riga in self.rows:
      for colonna in self.cols:
        for direction in [0, 1]:  # 0 = orizzontale, 1 = verticale
          if self.check_ship_placement(ship, riga, colonna, direction):
            positions.append((riga, colonna, direction))
    return positions