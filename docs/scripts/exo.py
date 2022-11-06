voyelles = ["a", "e", "i", "o", "u", "y"]


def dentiste(texte):
    resultat = ""
    for lettre in texte:
        if lettre in voyelles:
            resultat = resultat + lettre
    return resultat


assert dentiste("j'ai mal") == "aia"
assert dentiste("il fait chaud") == "iaiau"
assert dentiste("") == ""
