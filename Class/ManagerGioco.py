from Class.Flotta import *
from Class.Nave import *
from Class.Arsenale import *
from Class.Arma import *
from Class.Paese import *
from Class.Contatore_turni import *
from Class.AI import AI
import random
from Class.App_state import State

class GameManager:
  def __init__(self):
    self.colori_navi = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫",
                        "⚪", "🟥", "🟧", "🟨", "🟩", "🟦", "🟦", "🟫",
                        "⬛", "⬛", "🔺", "🔺"]
    self.AppState = State()

  def app_state(self) -> State:
    """
    Restituisce lo stato dell'applicazione.
    """
    return self.AppState
  
  def create_countries(self):
    """
    In questa funzione creiamo i 6+1 paesi fra i quali scegliere per giocare.
    """
    # Generiamo i paesei uno ad uno
    # Italia
    index = -1
    flotta = Navy()
    ship = Ship("MAS 526", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Circe", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Pegaso", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Saetta", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Folgore", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Turbine", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Luigi Cadorna", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Giovanni dalle Bande Nere", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Alberto di Giussano", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = Radar()
    Arsenale_tmp.add_weapon(w)
    w = AttaccoASorpresa()
    Arsenale_tmp.add_weapon(w)
    w = MinaSottomarina()
    Arsenale_tmp.add_weapon(w)
    self.Italy = Country("Italia", flotta, Arsenale_tmp)
    
    # Giappone
    index = -1
    flotta = Navy()
    ship = Ship("Ha-19", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Akebono", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Shiratsuyu", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Sendai", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Jintsu", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Fuso", 4, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Yamashiro", 4, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = AttaccoASorpresa()
    Arsenale_tmp.add_weapon(w)
    w = AttaccoASorpresa()
    Arsenale_tmp.add_weapon(w)
    w = FlottaEmergenza()
    Arsenale_tmp.add_weapon(w)
    w = FlottaEmergenza()
    Arsenale_tmp.add_weapon(w)
    self.Japan = Country("Giappone", flotta, Arsenale_tmp)
    
    # Germania
    index = -1
    flotta = Navy()
    ship = Ship("Scharnhorst", 4, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Gneisenau", 4, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Bismarck", 5, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Tirpitz", 5, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = Radar()
    Arsenale_tmp.add_weapon(w)
    w = Radar()
    Arsenale_tmp.add_weapon(w)
    self.Germany = Country("Germania", flotta, Arsenale_tmp)
    
    # URS
    index = -1
    flotta = Navy()
    ship = Ship("Gremyashchy", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Storozhevoy", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Kirov", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Voroshilov	", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Maxim Gorky", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Kalinin", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("Molotov", 3, self.colori_navi[index := index + 1]) # MANCA IL NOME
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = BombaAtomica()
    Arsenale_tmp.add_weapon(w)
    w = FlottaEmergenza()
    Arsenale_tmp.add_weapon(w)
    self.URS = Country("URS", flotta, Arsenale_tmp)
    
    # USA
    index = -1
    flotta = Navy()
    ship = Ship("PT-109", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("PT-59", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Fletcher", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Laffey	", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS O'Bannon", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Johnston", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Kidd", 2, self.colori_navi[index := index + 1]) # MANCA IL NOME
    flotta.add_ship(ship)
    ship = Ship("USS San Diego", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Helena	", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Atlanta", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Cleveland", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("USS Brooklyn", 3, self.colori_navi[index := index + 1]) # MANCA IL NOME
    flotta.add_ship(ship)
    ship = Ship("USS North Carolina", 4, self.colori_navi[index := index + 1]) # MANCA IL NOME
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = BombaAtomica()
    Arsenale_tmp.add_weapon(w)
    w = BombaAtomica()
    Arsenale_tmp.add_weapon(w)
    w = FlottaEmergenza()
    Arsenale_tmp.add_weapon(w)
    self.USA = Country("USA", flotta, Arsenale_tmp)
    
    # Regno Unito
    index = -1
    flotta = Navy()
    ship = Ship("MTB 102", 1, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("HMS Maori", 2, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("HMS Dido", 3, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("HMS Repulse	", 4, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("HMS Hood", 5, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    ship = Ship("HMS King George V", 5, self.colori_navi[index := index + 1])
    flotta.add_ship(ship)
    Arsenale_tmp = Arsenal()
    w = BombaAtomica()
    Arsenale_tmp.add_weapon(w)
    w = FlottaEmergenza()
    Arsenale_tmp.add_weapon(w)
    self.UnitedKingdom = Country("Regno Unito", flotta, Arsenale_tmp)

    # Creiamo un dizionario per i paesi per avere un accesso più rapido
    self.countries = {
      "Italia": self.Italy,
      "Giappone": self.Japan,
      "Germania": self.Germany,
      "URS": self.URS,
      "USA": self.USA,
      "Regno Unito": self.UnitedKingdom
    }
    
    # Rolla una possibilità per il paese della Repubblica di San Marino
    if random.randint(1, 100) <= 11:  # 11% di probabilità di giocare con la Repubblica di San Marino
      # Repubblica di San Marino
      index = -1
      flotta = Navy()
      ship = Ship("SM Riminese", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Maranello", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Garibaldi Bis", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Titanicio", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Frittata", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Cacciapizze", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Tricolore", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Panettone", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Polentiera", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Serenissima", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      ship = Ship("SM Confetto", 1, self.colori_navi[index := index + 1])
      flotta.add_ship(ship)
      Arsenale_tmp = Arsenal()
      for _ in range(11):
        w = FlottaEmergenza()
        Arsenale_tmp.add_weapon(w)
      self.SanMarino = Country("Repubblica di San Marino", flotta, Arsenale_tmp)
      self.countries["Repubblica di San Marino"] = self.SanMarino
    
  
  def get_countries(self) -> list:
    """
    Restituisce una lista dei nomi dei paesi disponibili.
    """
    return list(self.countries.keys())
    
    
  def get_country(self, country_name:str) -> Country:
    """
    Restituisce un paese in base al nome.
    """
    return self.countries[country_name] if country_name in self.countries else None
    
    
  def setup_settings(self, dim:int, diff:str, country_player:str, country_ai:str) -> None:
    """
    Inizializza tutto per una partita con il paese specificato.
    """
    # Inizializza i paesi dei giocatori
    self.player_country = self.get_country(country_player)
    self.ai_country = self.get_country(country_ai)
    self.ai_country.arsenal_ai()  # Reset dell'arsenale dell'AI
    
    self.map_size = dim
    self.griglia_player = Grid(self.map_size, "Player")
    self.griglia_ai = Grid(self.map_size, "AI")
    self.difficulty = diff
    self.turn_counter = Turn_counter()
    
    # Inizializza l'AI
    self.ai = AI(self.griglia_player, self.ai_country.get_arsenal(), self.difficulty)
    
  
  def riempimento_navi_ai(self, flotta:Navy) -> None:
    """
    Riempie la flotta dell'AI con navi casuali.
    """
    for S in flotta:
      posizioni = self.griglia_ai.possible_positions(S)
      pos = random.choice(posizioni)
      self.griglia_ai.ship_placement(S, pos[0], pos[1], pos[2])
  
  
  def controlla_posizione_nave_player(self, nave:Ship, riga:int, colonna:str, orientamento:str) -> bool:
    """
    Controlla se una nave può essere posizionata nella griglia del giocatore.
    """
    return self.griglia_player.check_ship_placement(nave, riga, colonna, orientamento)
  
  
  def posiziona_nave_player(self, nave:Ship, riga:int, colonna:str, orientamento:int):
    """
    Posiziona una nave nella griglia del giocatore.
    Questo perché il player deve scegliere la posizione delle navi, quindi le mette una per volta.
    """
    self.griglia_player.ship_placement(nave, riga, colonna, orientamento)
  
      
  def get_player_grid(self) -> Grid:
    """
    Restituisce la griglia del giocatore.
    """
    return self.griglia_player
  
  def get_ai_grid(self) -> Grid:
    """
    Restituisce la griglia dell'AI.
    """
    return self.griglia_ai
  
  
  def check_match_end(self) -> bool:
    """
    Controlla se la partita è finita.
    La partita finisce quando una delle flotte è stata distrutta.
    """
    return self.player_country.get_navy().end() or self.ai_country.get_navy().end()
  
  
  def turno(self) -> str:
    """
    Restituisce il turno corrente. ("Player" o "AI")
    """
    return self.turn_counter.turno()
  
  
  def len_Match(self) -> int:
    """
    Restituisce la lunghezza della partita.
    """
    return self.turn_counter.get_len()
  
  
  def controllo_allarmi(self, cella_colpita) -> None:
    """
    Controlla gli allarmi e li disattiva se il turno corrente è scaduto.
    """
    allarmi = self.turn_counter.get_alarms()
    for cella in allarmi.keys():
      turno_disattivazione, arma = allarmi[cella]
      
      if self.turn_counter.get_len() > turno_disattivazione:
        self.turn_counter.remove_alarm(cella)
        
      if cella_colpita != None:
        cella_colpita = self.griglia_player.cell(cella_colpita[0], cella_colpita[1])
      elif cella_colpita == cella:
        # Se la cella colpita è quella dell'allarme, lo rimuoviamo dalla lista e lo attiviamo
        self.turn_counter.remove_alarm(cella)
        if arma.type() == "Mina sottomarina":
          arma.use(GM.player_country.get_arsenal())
          arma.remove_trap(self.griglia_ai.cell(cella[0], cella[1]))
          
        elif arma.type() == "Flotta di emergenza":
          if self.check_match_end():  # Controlla se la partita è finita, in tal caso non posiziona la nave
            return None
          nave = Ship("Flotta d'emergenza", 1, "⚓")
          self.player_country.get_navy().add_ship(nave)
          celle_libere = self.griglia_player.possible_positions(nave)
          cella = random.choice(celle_libere)
          self.posiziona_nave_player(nave, cella[0], cella[1], 0)
          
          
  def next_turn(self):
    """
    Vai al turno successivo
    """
    self.turn_counter.next_turn()
  
  
  def play_turn(self, mossa_player = None) -> None:
    """
    Gestisce il turno corrente.
    """
    if self.turno() == "Player":
      # Il giocatore fa la sua mossa, se la mossa è None significa che ha usato un'arma
      if mossa_player != None:
        if self.griglia_ai.cell(mossa_player[0], mossa_player[1]).hitted():
          self.turn_counter.lenMatch -= 1
        self.griglia_ai.hit(mossa_player[0], mossa_player[1])
        if self.griglia_ai.cell(mossa_player[0], mossa_player[1]).occupied():
          self.turn_counter.turn_on_hit()
      print(f"Mossa player: {mossa_player}")
      self.controllo_allarmi(mossa_player)
      if self.check_match_end():
        ### PARTITA FINITA ###
        pass
      self.next_turn()
    else:
      # L'AI fa la sua mossa
      self.ai.make_move()
      if self.check_match_end():
        ### PARTITA FINITA ###
        pass
      self.next_turn()

  ## BISOGNA GESTIRE I CASI DI VITTORIA
  #if self.player_country.get_navy().end():
  #  print("L'AI ha vinto!")
  #elif self.ai_country.get_navy().end():
  #  print("Il giocatore ha vinto!")
  
  def use_weapon(self, weapon, coords:tuple) -> None:
    """
    Usa un'arma specificata dal nome e dalle coordinate.
    """
    if weapon.type() == "Bomba Atomica":
      weapon.use(self.griglia_ai, coords)
      
    elif weapon.type() == "Radar":
      count = weapon.use(self.griglia_ai, coords)
      print(f"Il radar ha rilevato {count} navi nell'area.")
      
    elif weapon.type() == "Attacco a sorpresa":
      weapon.use(self.turn_counter)
      print("Hai usato un attacco a sorpresa, hai altri 2 turni a disposizione.")
      
    elif weapon.type() == "Mina sottomarina":
      try:
        weapon.set_trap(GM.turn_counter, GM.griglia_player.cell(coords[0], coords[1]))
      except ValueError as e:
        #print(f"Errore: {e}")
        return f"Errore: {e}"
    
    elif weapon.type() == "Flotta di emergenza":
      try:
        weapon.set_trap(GM.turn_counter, GM.griglia_player.cell(coords[0], coords[1]))
      except ValueError as e:
        return f"Errore: {e}"
      
      
      
      
      
      
      
      
      
      

if __name__ == "__main__":
  import time
  a = time.time()
  # Eseguiamo la creazione dei paesi
  GM = GameManager()
  GM.create_countries()
  
  GM.setup_settings(10, "Facile", "Italia", "Giappone")
  for nave in GM.player_country.get_navy():
    print(f"Iterazione per la nave: {nave.name} ({str(nave.dim())})")
    GM.posiziona_nave_player(nave, 1, "A", 0)
    break
  print(f"Griglia player: \n{GM.griglia_player.df()}")
  GM.riempimento_navi_ai(GM.ai_country.navy)
  
  print(GM.griglia_ai.df())
  
  X = [1, 2, 3, 4, 5, 6, 7, 8]
  Y = ["A", "B", "C", "D", "E", "F", "G", "H"]
  
  b = time.time()
  for x in X:
    for y in Y:
      GM.griglia_ai.hit(x, y)
  c = time.time()
  print(f"Tempo impiegato per fare tutto: {c - a} secondi")
  print(f"Tempo impiegato per colpire tutte le celle: {c - b} secondi")
  
  
  print(GM.griglia_ai.df())
  
  
  
  print(GM.turno())
  w = MinaSottomarina()
  print(w.type())
  GM.use_weapon(w, (3, "A"))
  print(GM.turn_counter.get_alarms())