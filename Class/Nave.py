class Ship:
  """
  Classe per la creazione della nave.
  """
  
  def __init__(self, name:str, length:int, col:str) -> None:
    """
    Inizializza la nave.
    """
    self.name = name
    self.length = length
    self.hitted_times = 0 # Numero di colpi subiti dalla nave
    self.col = col

  def __repr__(self) -> str:
    """
    Restituisce il colore che rappresenta la nave.
    """
    return self.col
  # OPPURE
  def get_col(self) -> str:
    """
    Restituisce il colore della nave.
    """
    return self.col

  def dim(self) -> int:
    """
    Restituisce la dimensione della nave.
    """
    return self.length
  
  def hit(self, already_hitted = False):
    """
    Colpisce la nave.
    Se la nave si trova in un gruppo di allarmi, attiva il potere dell'allarme.
    """
    if self.hitted_times < self.length and not already_hitted:
      self.hitted_times += 1
    #if self.hitted_times == self.length and self in gruppo_allarmi:
      # togli la nave affondata dalla lista degli allarmi
      # se la flotta è vuota non faccio nulla (metodo end)
      # altrimenti
      # crea una nave 1x1 e mettila nella flotta
      # piazzala a caso
      #pass
  
  def dead(self) -> bool:
    """
    Restituisce True se la nave è affondata, False altrimenti.
    """
    return self.hitted_times == self.length