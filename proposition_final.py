# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:51:14 2026

@author: celian.mludek
"""

# ------------------------------
# Projet Puissance 4 – NSI 2026
# ------------------------------

NB_LIGNES = 6
NB_COLONNES = 7
NB_PIONS_ALIGNES = 4
NIVEAU_MAX = 4  # profondeur maximale de l'arbre Min-Max

# ------------------------------
# Classe Grille
# ------------------------------
class Grille:
    def __init__(self):
        """Crée une grille vide 6x7"""
        self.grille = [[0 for _ in range(NB_COLONNES)] for _ in range(NB_LIGNES)]

    def joue(self, colonne, joueur):
        """Place un pion du joueur dans la colonne si possible"""
        ligne = NB_LIGNES - 1
        while ligne != -1 and self.grille[ligne][colonne] != 0:
            ligne -= 1
        if ligne != -1:
            self.grille[ligne][colonne] = joueur
            return True
        else:
            return False

    def est_pleine(self):
        """Retourne True si la grille est pleine"""
        return all(self.grille[i][j] != 0 for i in range(NB_LIGNES) for j in range(NB_COLONNES))

    def copie_grille(self):
        """Retourne une copie indépendante de la grille"""
        g = Grille()
        g.grille = [ligne.copy() for ligne in self.grille]
        return g

    def __repr__(self):
        """Affichage console de la grille"""
        s = ""
        for ligne in self.grille:
            s += "|" + "|".join(str(c) for c in ligne) + "|\n"
        return s

    def gagnant(self):
        """Retourne 0 si pas de gagnant, sinon 1 ou 2"""
        for joueur in [1,2]:
            # horizontal
            for i in range(NB_LIGNES):
                for j in range(NB_COLONNES - 3):
                    if all(self.grille[i][j+k] == joueur for k in range(4)):
                        return joueur
            # vertical
            for i in range(NB_LIGNES - 3):
                for j in range(NB_COLONNES):
                    if all(self.grille[i+k][j] == joueur for k in range(4)):
                        return joueur
            # diagonale descendante
            for i in range(NB_LIGNES - 3):
                for j in range(NB_COLONNES - 3):
                    if all(self.grille[i+k][j+k] == joueur for k in range(4)):
                        return joueur
            # diagonale montante
            for i in range(3, NB_LIGNES):
                for j in range(NB_COLONNES - 3):
                    if all(self.grille[i-k][j+k] == joueur for k in range(4)):
                        return joueur
        return 0

    def score(self):
        """Score = alignements J2 - J1 (simplifié ici)"""
        # pour simplifier, chaque pion vaut 1 point si dans un alignement de 4 possible
        def valeur_case(i,j):
            return 1
        total = 0
        for i in range(NB_LIGNES):
            for j in range(NB_COLONNES):
                if self.grille[i][j] == 2:
                    total += valeur_case(i,j)
                elif self.grille[i][j] == 1:
                    total -= valeur_case(i,j)
        return total

# ------------------------------
# Classe Noeud (Min-Max)
# ------------------------------
class Noeud:
    def __init__(self, colonne):
        self.colonne = colonne  # -1 pour racine
        self.score = 0
        self.suivants = []

    def colonne_score_min(self):
        return min(((n.colonne, n.score) for n in self.suivants), key=lambda x: x[1])

    def colonne_score_max(self):
        return max(((n.colonne, n.score) for n in self.suivants), key=lambda x: x[1])

    def calcule_score(self, niveau, joueur, grille):
        g = grille.gagnant()
        if g == 1:
            self.score = -(100 + 10*(NIVEAU_MAX - niveau))
        elif g == 2:
            self.score = 100 + 10*(NIVEAU_MAX - niveau)
        elif niveau == NIVEAU_MAX:
            self.score = grille.score()
        else:
            for colonne in range(NB_COLONNES):
                grille2 = grille.copie_grille()
                if grille2.joue(colonne, joueur):
                    nouveau_noeud = Noeud(colonne)
                    self.suivants.append(nouveau_noeud)
                    nouveau_noeud.calcule_score(niveau+1, 2 if joueur==1 else 1, grille2)
            if self.suivants:
                if joueur == 1:
                    self.score = min(n.score for n in self.suivants)
                else:
                    self.score = max(n.score for n in self.suivants)

# ------------------------------
# Fonction pour choisir le meilleur coup
# ------------------------------
def choisit_coup(grille, joueur):
    racine = Noeud(-1)
    racine.calcule_score(0, joueur, grille)
    if joueur == 1:
        return racine.colonne_score_min()[0]
    else:
        return racine.colonne_score_max()[0]

# ------------------------------
# Exemple de partie
# ------------------------------
if __name__ == "__main__":
    g = Grille()
    joueur = 1  # 1 = humain, 2 = IA

    while not g.est_pleine() and g.gagnant() == 0:
        print(g)
        if joueur == 1:
            col = int(input("Joueur 1, choisissez une colonne (0-6): "))
        else:
            col = choisit_coup(g, 2)
            print(f"IA joue colonne {col}")

        if g.joue(col, joueur):
            joueur = 2 if joueur == 1 else 1
        else:
            print("Colonne pleine, rejouez!")

    print(g)
    vainqueur = g.gagnant()
    if vainqueur == 0:
        print("Match nul!")
    else:
        print(f"Le joueur {vainqueur} a gagné!")