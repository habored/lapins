#--- HDR ---#
class Noeud:
    """
    Classe implémentant un nœud d'arbre disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre à gauche.
    - droite : le sous-arbre à droite.
    Par défaut les nœuds gauche et droit sont initialisés à None. 
    """
    def __init__(self, valeur, gauche = None, droite = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
#--- HDR ---#

def sélectionne(r, x):
    """ Renvoie le noeud d'étiquette x dans l'arbre de racine r. 
    Renvoie None si x n'est pas présent dans l'arbre de racine r."""
    if r is None:
        return None
    else:
        if ...:
            return r
        else:
            à_gauche = sélectionne(r.gauche, x)
            if ...:
                return ...
            else:
                return ...

def compte_éléments(r):
    """ Détermine le nombre d'éléments de l'arbre de racine r. """
    if r is None:
        return ...
    else:
        return ...

def est_gagnable(r, n, x):
    """ Détermine s'il est possible de gagner la partie avec 
    l'arbre de racine r, de taille n, le premier joueur ayant joué x. """
    # On sélectionne le nœud choisit par le joueur 1.
    noeud = ...
    # On compte le nombre de nœuds présents dans le sous-arbre gauche
    # du nœud choisit par le joueur 1. 
    noeud_taille_gauche = ...
    # On compte le nombre de nœuds présents dans le sous-arbre droit
    # du nœud choisit par le joueur 1. 
    noeud_taille_droit = ...
    # On compte le nombre de nœuds qui ne sont pas dans l'arbre de racine
    # noeud mais qui sont dans l'arbre de racine r. 
    noeud_taille_above = ...

    # Si jamais il y a plus de nœuds dans le sous-arbre gauche de noeud
    # que dans le reste de l'arbre, alors on peut gagner en en sélectionnant
    # la racine.
    # etc.
    return noeud_taille_gauche > 1 + ... + ... or ... > ... or ... > ...


# Tests

r = Noeud(1,
          Noeud(2,
                Noeud(3),
                None),
          Noeud(4,
                None,
                Noeud(5)))

assert sélectionne(None, 42) == None
for i in range(1, 5):
    assert sélectionne(r, i).valeur == i 
assert sélectionne(r, 0) == None

assert compte_éléments(r) == 5
assert compte_éléments(sélectionne(r, 2)) == 2
assert compte_éléments(sélectionne(r, 3)) == 1

assert est_gagnable(r, 5, 2) == True
assert est_gagnable(r, 5, 1) == False
assert est_gagnable(r, 5, 5) == True
