def appartient(animal, ferme):
    return animal in ferme


ferme_gaston = {"lapin": 5, "vache": 7, "cochon": 2, "cheval": 4}

# Tests
assert (
    appartient("oie", ferme_gaston) == False
), "oie n'est pas une clé de ce dictionnaire"
assert appartient("oie", ferme_gaston) == True

# Ajoutez vos essais ci-dessous en mettant un message dans le assert:
