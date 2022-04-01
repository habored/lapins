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

r =  Noeud(1,
           Noeud(2,
                 Noeud(4,
                       Noeud(8),
                       Noeud(9)),
                 Noeud(5,
                       Noeud(10),
                       Noeud(11))),
           Noeud(3,
                 Noeud(6),
                 Noeud(7)))
assert est_gagnable(r, n, 1) == True
assert est_gagnable(r, n, 2) == False
assert est_gagnable(r, n, 5) == True
