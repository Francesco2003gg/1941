## Gestiamo lo stato dell'applicazione in un gioco di battaglia navale utilizzando lo State Design Pattern.
from dataclasses import dataclass

class AppState():
  """
  Una clsse per gestire lo stato dell'applicazione.
  """
  def go_to_settings(self):
    ...
    
  def go_to_placing(self):
    ...
    
  def go_to_match(self):
    ...
    
  def go_to_WinnerScreen(self):
    ...
  
  def go_to_LoserScreen(self):
    ...
    
@dataclass
class Access:
  app_state: AppState
  
  def go_to_settings(self):
    print("Stai andando alla schermata delle impostazioni.")
    self.app_state.set_state(Settings(self.app_state))
    
  def go_to_placing(self):
    print("ERRORE! Sei nell'accesso, non puoi piazzare le navi.")
    
  def go_to_match(self):
    print("ERRORE! Sei nell'accesso, non puoi iniziare una partita.")
    
  def go_to_WinnerScreen(self):
    print("ERRORE! Sei nell'accesso, non puoi andare alla schermata del vincitore.")
  
  def go_to_LoserScreen(self):
    print("ERRORE! Sei nell'accesso, non puoi andare alla schermata del perdente.")


@dataclass
class Settings:
  app_state: AppState
  
  def go_to_settings(self):
    print("ERRORE! Sei già nella schermata delle impostazioni.")
    
  def go_to_placing(self):
    print("Stai andando alla schermata di piazzamento delle navi.")
    self.app_state.set_state(Placing(self.app_state))
    
  def go_to_match(self):
    print("ERRORE! Sei nelle impostazioni, non puoi iniziare una partita.")
    
  def go_to_WinnerScreen(self):
    print("ERRORE! Sei nelle impostazioni, non puoi andare alla schermata del vincitore.")
  
  def go_to_LoserScreen(self):
    print("ERRORE! Sei nelle impostazioni, non puoi andare alla schermata del perdente.")


@dataclass
class Placing:
  app_state: AppState
  
  def go_to_settings(self):
    print("Stai tornando alla schermata delle impostazioni.")
    self.app_state.set_state(Settings(self.app_state))
    
  def go_to_placing(self):
    print("ERRORE! Sei già nella schermata di piazzamento.")
    
  def go_to_match(self):
    print("Stai andando alla schermata di partita.")
    self.app_state.set_state(Match(self.app_state))
    
  def go_to_WinnerScreen(self):
    print("ERRORE! Sei nella schermata di piazzamento, non puoi andare alla schermata del vincitore.")
  
  def go_to_LoserScreen(self):
    print("ERRORE! Sei nella schermata di piazzamento, non puoi andare alla schermata del perdente.")


@dataclass
class Match:
  app_state: AppState
  
  def go_to_settings(self):
    print("ERRORE! Sei in partita, non puoi andare alle impostazioni.")
    
  def go_to_placing(self):
    print("ERRORE! Sei in partita, non puoi piazzare le navi.")
    
  def go_to_match(self):
    print("ERRORE! Sei già nella schermata di partita.")
    
  def go_to_WinnerScreen(self):
    print("Stai andando alla schermata del vincitore.")
    self.app_state.set_state(WinnerScreen(self.app_state))
  
  def go_to_LoserScreen(self):
    print("Stai andando alla schermata del perdente.")
    self.app_state.set_state(LoserScreen(self.app_state))


@dataclass
class WinnerScreen:
  app_state: AppState
  
  def go_to_settings(self):
    print("Stai tornando alla schermata delle impostazioni.")
    self.app_state.set_state(Settings(self.app_state))
    
  def go_to_placing(self):
    print("ERRORE! Sei nella schermata del vincitore, non puoi piazzare le navi.")
    
  def go_to_match(self):
    print("ERRORE! Sei nella schermata del vincitore, non puoi iniziare una partita.")
    
  def go_to_WinnerScreen(self):
    print("ERRORE! Sei già nella schermata del vincitore.")
  
  def go_to_LoserScreen(self):
    print("ERRORE! Sei nella schermata del vincitore, non puoi andare alla schermata del perdente.")


@dataclass
class LoserScreen:
  app_state: AppState
  
  def go_to_settings(self):
    print("Stai tornando alla schermata delle impostazioni.")
    self.app_state.set_state(Settings(self.app_state))
    
  def go_to_placing(self):
    print("ERRORE! Sei nella schermata del perdente, non puoi piazzare le navi.")
    
  def go_to_match(self):
    print("ERRORE! Sei nella schermata del perdente, non puoi iniziare una partita.")
    
  def go_to_WinnerScreen(self):
    print("ERRORE! ei nella schermata del perdente, non puoi andare alla schermata del vincitore.")
  
  def go_to_LoserScreen(self):
    print("ERRORE! Sei già nella schermata del perdente.")


class State:
  def __init__(self):
    self.state: AppState = Access(self)
    print("Stato iniziale: Accesso")
    
  def set_state(self, state: AppState):
    """
    Imposta lo stato dell'applicazione.
    
    Input:
    - state: lo stato da impostare
    """
    self.state = state
    
  def get_state(self) -> AppState:
    """
    Restituisce lo stato corrente dell'applicazione.
    
    return:
    - state: lo stato corrente
    """
    return type(self.state)
  
  def go_to_settings(self):
    """
    Va alla schermata delle impostazioni.
    """
    self.state.go_to_settings()
    
  def go_to_placing(self):
    """
    Va alla schermata di piazzamento delle navi.
    """
    self.state.go_to_placing()
  
  def go_to_match(self):
    """
    Va alla schermata di partita.
    """
    self.state.go_to_match()
  
  def go_to_WinnerScreen(self):
    """
    Va alla schermata del vincitore.
    """
    self.state.go_to_WinnerScreen()
    
  def go_to_LoserScreen(self):
    """
    Va alla schermata del perdente.
    """
    self.state.go_to_LoserScreen()
    
def test() -> None:
  """
  Funzione principale per testare lo stato dell'applicazione.
  """
  App = State()
  #Accesso iniziale
  
  print("Da qui parte il testing dello stato dell'applicazione")
  App.go_to_match()  # ERRORE!

  App.go_to_settings()  # Accesso alle impostazioni
  App.go_to_LoserScreen()  # ERRORE! 
  App.go_to_placing()    # Piazzamento delle navi
  App.go_to_match()      # Inizio della partita
  App.go_to_settings()    # ERRORE!
  
  App.go_to_WinnerScreen() # Schermata del vincitore
  App.go_to_LoserScreen()   # Schermata del perdente
  
  print(App.get_state() == WinnerScreen)  # Verifica dello stato corrente
  print(App.get_state() == LoserScreen)  # Verifica dello stato corrente
  
  
  
if __name__ == "__main__":
    test()