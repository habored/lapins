import random

def calculer_déplacement_zèbre():
    if random.random() > 1 / 2:
        déplacement = 6
    else:
        déplacement = -1
    return déplacement