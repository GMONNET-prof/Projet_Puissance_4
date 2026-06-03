from random import randint

NB_LIGNE = 12
NB_COLONNE = 12

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class puissance4:
    def __init__(self, player):
        self.grid = [[0 for _ in range(NB_COLONNE)] for _ in range(NB_LIGNE)]
        self.playerColor = player
    
    def playMove(self, col, value):
        row = NB_LIGNE - 1 
        while row != -1 and self.grid[row][col] != 0:
            row -= 1
        if row != -1:
            self.grid[row][col] = value
            return True
        else: 
            return False

    def __repr__(self):
        symbols = {
            0: "● ",
            1: f"{bcolors.WARNING}● {bcolors.ENDC}",
            2: f"{bcolors.FAIL}● {bcolors.ENDC}",
        }

        width = len(self.grid[0])
        border = "─" * (width * 2 + 1)

        return "\n".join([
            " " + "".join(f" {i}" for i in range(width)),
            f"╭{border}╮",
            *("│ " + "".join(symbols[v] for v in row) + "│" for row in self.grid),
            f"╰{border}╯",
        ])
        print(f"Vous êtes le joueur {self.playerColor}")

    def verifier_horizontalement(self, player):
        for ligne in self.grid:
            for i in range(len(ligne)-2):
                print(ligne[i])
                if ligne[i] == player and ligne[i] == ligne[i+1] and ligne[i+1] == ligne[i+2] and ligne[i+2] == ligne[i+3]:
                    return True
        return False
    

def play(grid, player = 1):
    while True:
        print(grid)
        try:
            move = int(input(f"Joueur {player}, Entrez l'indice de votre coup: "))
            if 0 <= move < NB_COLONNE:
                if grid.playMove(move, player):
                    player = (player % 2) + 1
                    print(grid.verifier_horizontalement(player))
                    continue
        except ValueError:
            pass
        print("Indice invalide.")

        
test = puissance4(1)
play(test)
