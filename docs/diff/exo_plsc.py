memoire = {}

def plus_longue_sous_chaine(texte1, texte2):
    if len(texte1) == 0 or len(texte2) == 0:
        return ...

    if (texte1, texte2) in memoire:
        return ...

    if texte1[-1] == ...:
        memoire[(texte1, texte2)] = plus_longue_sous_chaine(..., ...) + texte1[-1]
    else:
        cas_1 = plus_longue_sous_chaine(..., ...)
        cas_2 = plus_longue_sous_chaine(..., ...)

        if len(cas_1) >= len(cas_2):
            memoire[(texte1, texte2)] = ...
        else:
            memoire[(texte1, texte2)] = ...

    return ...


# Fonction plus_longue_sous_chaine
texte1 = "merssi de respecté l'ortaugrafe !"
texte2 = "Merci de respecter l'orthographe !"
assert plus_longue_sous_chaine(texte1, texte2) == "eri de respect l'ortgrae !"
texte1 = "lapin"
texte2 = "caprin"
assert plus_longue_sous_chaine(texte1, texte2) == "apin"
texte1 = "abcd"
texte2 = "abcde"
assert plus_longue_sous_chaine(texte1, texte2) == "abcd"
texte1 = "aBaBaBaB"
texte2 = "aaaa"
assert plus_longue_sous_chaine(texte1, texte2) == "aaaa"
