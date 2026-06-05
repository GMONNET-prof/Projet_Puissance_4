# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:59:41 2026

@author: celian.mludek
"""

def est_pleine(self):
    """"retourne False si la grille n'est pas pleine et True si elle est pleine
    Entrer :  
    Sortie : booleen (bool) """
    
    for laliste in self.grille:
        for j in laliste:
            if j == 0:
                return False
    return True