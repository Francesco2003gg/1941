from Class.Griglia import Grid
from Class.Contatore_turni import Turn_counter

class Weapon:
  def __init__(self, name:str, power:int) -> None:
    self.name = name
    self.power = power
    self.used = False
  
  def type(self) -> str:
    return self.name
  
  def get_power(self) -> float:
    return self.power
  
  def used(self) -> bool:
    return self.used
  
  # metodo astratto per l'uso delle armi, va implementato nelle classi che ereditano
  def use(self, grid, coords):
    pass


class BombaAtomica(Weapon):
  def __init__(self):
      super().__init__("Bomba Atomica", 9)

  def use(self, grid:Grid, coords:tuple) -> None:
    x, y = coords
    print(f"Uso una bomba con coordinate {coords}")
    if type(y) == str:
      y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"].index(y)
    for dx in range(2):
      for dy in range(2):
        grid.hit(x + dx, y + dy)
    self.used = True


class Radar(Weapon):
  def __init__(self):
    super().__init__("Radar", 7)

  def use(self, grid:Grid, coords:tuple) -> int:
    x, y = coords
    if type(y) == str:
      y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"].index(y)
    count = 0
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        if grid.occupied(x + dx, y + dy):
          count += 1
    self.used = True
    return count
  

class AttaccoASorpresa(Weapon):
  def __init__(self):
    super().__init__("Attacco a sorpresa", 4)
    
  def use(self, TurnCounter) -> None:
    # Incrementiamo il contatore dei turni
    TurnCounter.turn_on_hit()
    TurnCounter.turn_on_hit()
    self.used = True


class MinaSottomarina(Weapon):
  """
  Classe per la creazione della mina sottomarina.
  Ricordando che va inserita nel dizionario degli allarmi
  - La chiave deve essere la CELLA in cui è stata piazzata.
  - Il valore è una tupla contentente (turno_di_disattivazione, oggetto di tipo arma).
  """
  def __init__(self):
    super().__init__("Mina sottomarina", 2.5)
    self.durata = 10

  def set_trap(self, TurnCounter:Turn_counter, cell):
    if cell.occupied() or cell.hitted():
      raise ValueError("La cella deve essere vuota e non colpita per piazzare una mina sottomarina.")
    TurnCounter.set_alarm(cell, self.durata, self)
    self.used = True
  
  def use(self, arsenale) -> None:
    w = AttaccoASorpresa()
    arsenale.add_wewapon(w)


class FlottaEmergenza(Weapon):
  """
  Classe per la creazione della flotta d'emergenza.
  Ricordando che va inserita nel dizionario degli allarmi
  - La chiave deve essere la CELLA in cui è stata piazzata.
  - Il valore è una tupla contentente (turno_di_disattivazione, oggetto di tipo arma).
  """
  def __init__(self):
    super().__init__("Flotta d'emergenza", 6)
    self.durata = 10

  def set_trap(self, TurnCounter:Turn_counter, cell):
    if not cell.occupied() or cell.hitted():
      raise ValueError("La cella deve essere occupata e non colpita per piazzare una 4flotta d'emergenza.")
    TurnCounter.set_alarm(cell, self.durata, self)
    self.used = True
    
  def use(self, grid:Grid, coords:tuple) -> None:
    ... # Implementazione dell'uso della flotta d'emergenza
