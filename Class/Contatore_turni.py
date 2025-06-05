class Turn_counter:
  """
  Classe per il conteggio dei turni.
  """
  
  def __init__(self):
    """
    Inizializza il contatore dei turni.
    Inizia sempre il player, quindi inizializziamo il turno a 1.
    Turni:
    . -1: AI
    . +1: Player
    """
    self.turn = 1
    self.lenMatch = 0 # Lunghezza della partita
    self.alarms = dict() # Lista di allarmi (Chiave: Cella,
                         #                   Valore: (Turno di disattivazione, Arma) )
    
  def turno(self):
    """
    Restituisce il turno corrente.
    """
    return "Player" if self.turn > 0 else "AI"
  
  def next_turn(self):
    """
    Passa al turno successivo.
    Diminuisce il numero di turni rimanenti per gli allarmi.
    """
    self.turn += 2 if self.turn < 0 else -2
    self.lenMatch += 1
    #for i in self.alarms.keys():
    #  self.alarms[i] -= 1
    #  if self.alarms[i] <= 0:
    #    del self.alarms[i]
  
  def turn_on_hit(self):
    """
    Funzione che serve per far giocare nuovamente il giocatore se colpisce una nave.
    """
    self.turn += -2 if self.turn < 0 else 2
    
  def add_len(self):
    """
    Aggiunge 1 alla lunghezza della partita.
    """
    self.lenMatch += 1
    
  def get_len(self):
    """
    Restituisce la lunghezza della partita.
    """
    return self.lenMatch
  
  def set_alarm(self, cella, durata, arma=None):
    """
    Imposta un allarme.
    key: Cella in cui si trova l'allarme;
    value: Tuple(turno di disattivazione, arma)
    """
    self.alarms[cella] = (self.lenMatch + durata, arma)
    
  def get_alarms(self):
    """
    Restituisce il dizionario con tutti gli allarmi attivi.
    """
    return self.alarms
  
  def remove_alarm(self, cella):
    """
    Rimuove un allarme.
    
    cella: Cella in cui si trova l'allarme da rimuovere.
    """
    del self.alarms[cella]