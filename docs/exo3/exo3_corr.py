import random

def calculer_déplacement_zèbre():
    if random.random() > 1 / 2:
        déplacement = 6
    else:
        déplacement = -1
    return déplacement

def calculer_déplacement_lion():
    # notation if/else adaptée pour une unique instruction
    if random.random() > 1 / 2: déplacement = 5
    else: déplacement = 0
    return déplacement

def calculer_déplacement_éléphant():
    # notation if/else adaptée pour une unique instruction
    if random.random() > 1 / 4: déplacement = 2
    else: déplacement = 4
    return déplacement