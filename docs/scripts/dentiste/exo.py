voyelles = ["a", "e", "i", "o", "u", "y"]


def dentiste(texte):
    return "".join(c for c in texte if c in "aeiouy")


# Tests
assert dentiste("j'ai mal") == "aia"
assert dentiste("il fait chaud") == "iaiau"
assert dentiste("") == ""
