# Projet_Puissance_4

Jeu du **Puissance 4** à deux joueurs (humain VS humain puis humain VS machine).  
Ce projet est développé en **Python** et permet de jouer directement depuis la console.

---

## Contenu du projet

Le projet est principalement structuré autour de la **classe Grille**, qui gère la logique du jeu, et de plusieurs fonctions associées pour vérifier les conditions de victoire et jouer une partie complète.

---

## Classes et Fonctions

### Classe `Grille`

| Fonction | Entrée | Sortie | Description | Auteur | Priorité |
|----------|--------|--------|------------|--------|----------|
| `__init__` | Aucune | Aucune | Initialise la grille remplie de zéros | - | 1 |
| `jouer` | `colonne` (int), `joueur` (int) | Booléen | Met à jour la grille et retourne `True` si tout s’est bien passé, `False` sinon | - | 1 |
| `__repr__` | Aucune | `str` | Affiche la grille dans la console | - | 1 |
| `score` | Aucune | int | Renvoie le score du joueur 2 : nombre d’alignements du joueur 2 – nombre d’alignements du joueur 1 | - | 1 |
| `verifier_verticalement` | `joueur` (int) | Booléen | Retourne `True` si le joueur a gagné verticalement | JOAN / NOAH | 1 |
| `verifier_horizontalement` | `joueur` (int) | Booléen | Retourne `True` si le joueur a gagné horizontalement | BARDIA / LOUKA / Celian | 1 |
| `verifier_diagonale1` | `joueur` (int) | Booléen | Retourne `True` si le joueur a gagné en diagonale descendant | MATHIS / NICOLAS | 1 |
| `verifier_diagonale2` | `joueur` (int) | Booléen | Retourne `True` si le joueur a gagné en diagonale montant | YOHAN / FANNIE | 1 |
| `a_gagne` | Aucune | int | Parcourt la grille et retourne le numéro du gagnant (0, 1 ou 2) | - | 2 |
| `lancer_la_partie` | Aucune | Aucune | Lance la partie : tant que personne n’a gagné, interroge les joueurs sur leurs coups | - | 3 |
| `est_pleine` | Aucune | Booléen | Vérifie s’il reste encore des cases vides dans la grille | CELIAN | 3 |

---

### Classe `Noeud`

*La classe `Noeud` est prévue pour gérer la logique des arbres de décision si une IA est implémentée, mais n’a pas encore de détails complets dans ce projet.*

---

### Fonctions externes

*Des fonctions supplémentaires peuvent être ajoutées pour améliorer le jeu, gérer l’interface, ou calculer des stratégies pour l’IA.*

---

## Exemple d’utilisation

```python
from puissance4 import Grille

grille = Grille()
grille.lancer_la_partie()
