from random import *
from Class.Griglia import Grid
from Class.Arsenale import Arsenal

class AI:
    """
    Classe per la gestione dell'intelligenza artificiale nel gioco della Battaglia Navale.
    """

    def __init__(self, grid_player: Grid, Arsenale_ai:Arsenal, difficulty:str) -> None:
        """
        Inizializza l'AI con la griglia di gioco.
        """
        self.grid_player = grid_player
        self.difficulty = difficulty
        self.p = 0.05 if difficulty == "Facile" else 0.1 if difficulty == "Normale" else 0.16
        self.arsenal = Arsenale_ai  # Arsenal dell'AI
            
        self.last_hit = None  # Ultima cella colpita
        self.targeted_cells = []  # Celle già colpite
        self.ships_sunk = []  # Celle con Navi colpite

    def make_move(self) -> tuple:
        """
        Genera una mossa casuale per l'AI.
        """
        #Rolliamo la probabilità di usare un'arma speciale, se disponibili
        if not self.arsenal.empty() and randint(0, 100) <= self.p * 100:
            weapon_to_use = self.arsenal.still_usable().pop()
            cells_to_bomb = [c for c in self.hittable_cells() if self.grid_player.check_attack(c[0], c[1], type=2)]
            print(f"Celle che si possono colpire con bombe: {cells_to_bomb}")
            weapon_to_use.use(self.grid_player, choice(cells_to_bomb))
        # Se non usiamo una bomba atomica, procediamo con la logica seguente
        
        elif self.difficulty == "Facile":
            to_hit = self.random_move()
            self.grid_player.hit(to_hit[0], to_hit[1])
            if self.grid_player.occupied(to_hit[0], to_hit[1]):
                self.ships_sunk.append(to_hit)
            self.targeted_cells.append(to_hit)
        
        else:
            if self.last_hit == None:
                if self.difficulty == "Difficile":
                    if randint(0, 1) == 0:
                        to_hit = choice([c for c in self.hittable_cells() if self.grid_player.occupied(c[0], c[1])])
                    else:
                        to_hit = self.random_move()
                else:
                    to_hit = self.random_move()
                print("Mossa scelta senza controllo")
                self.grid_player.hit(to_hit[0], to_hit[1])
                if self.grid_player.occupied(to_hit[0], to_hit[1]):
                    self.ships_sunk.append(to_hit)
                    self.last_hit = to_hit
                self.targeted_cells.append(to_hit)
            else:
                row, col = self.last_hit
                if type(col) == str:
                    col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"].index(col)
                directions = ["up", "down", "left", "right"]
                print("Inizio i controlli delle direzioni")
                for direction in directions:
                    print(f"Inizio il controllo per {direction}")
                    next_cell = self.check_direction(row, col, direction)
                    print(f"Controllo finito, scelta{next_cell}")
                    if next_cell:
                        self.grid_player.hit(next_cell[0], next_cell[1])
                        if self.grid_player.occupied(next_cell[0], next_cell[1]):
                            self.ships_sunk.append(next_cell)
                            if self.grid_player.ship_dead(self.last_hit[0], self.last_hit[1]):
                                self.last_hit = None
                        self.targeted_cells.append(next_cell)
                        return next_cell

        
    
    def hittable_cells(self) -> list:
        """
        Restituisce le celle che possono essere colpite dall'AI.
        """
        hittable = []
        for row in self.grid_player.rows:
            for col in self.grid_player.cols:
                if self.grid_player.cell(row, col).hittable():
                    hittable.append((row, col))
        return hittable
    
    def random_move(self) -> tuple:
        """
        Genera una mossa casuale per l'AI, utilizzando un'arma speciale se disponibile.
        """
        return choice(self.hittable_cells())
    
    def check_direction(self, row:int, col:int, direction:str):
        """
        Controlla se il continuo di una nave si trova in una certa direzione.
        
        Input:
        - row: riga della cella;
        - col: colonna della cella;
        - direction: direzione ("up", "down", "left", "right");
        
        Output:
        - Una tupla (row, col) se la cella è valida per il continuo della nave;
        - False se non è valida o se non esiste un continuo in quella direzione.
        """
        if direction == "up":
            if row == 0:
                return False
            i = 0
            while True:
                i -= 1
                if row+i <= 0:
                    return False
                elif (row+i, col) in self.targeted_cells and (row+i, col) not in self.ships_sunk:
                    return False
                elif (row+i, col) in self.targeted_cells and (row+i, col) in self.ships_sunk:
                    continue
                else:
                    return (row+i, col)
                
        elif direction == "down":
            if row == self.grid_player.dim() - 1:
                return False
            i = 1
            while True:
                if row+i >= self.grid_player.dim():
                    return False
                if (row+i, col) in self.targeted_cells and (row+i, col) not in self.ships_sunk:
                    return False
                elif (row+i, col) in self.targeted_cells and (row+i, col) in self.ships_sunk:
                    i += 1
                    continue
                else:
                    return (row+i, col)
                
        elif direction == "left":
            if col == 0:
                return False
            i = -1
            while True:
                if col+i < 0:
                    return False
                if (row, col+i) in self.targeted_cells and (row, col+i) not in self.ships_sunk:
                    return False
                elif (row, col+i) in self.targeted_cells and (row, col+i) in self.ships_sunk:
                    i -= 1
                    continue
                else:
                    return (row, col+i)
                
        elif direction == "right":
            if col == self.grid_player.dim() - 1:
                return False
            i = 1
            while True:
                if col+i >= self.grid_player.dim():
                    return False
                if (row, col+i) in self.targeted_cells and (row, col+i) not in self.ships_sunk:
                    return False
                elif (row, col+i) in self.targeted_cells and (row, col+i) in self.ships_sunk:
                    i += 1
                    continue
                else:
                    return (row, col+i)
            