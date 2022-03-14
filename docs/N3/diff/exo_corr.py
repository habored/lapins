def sans_dernier(texte):
    assert len(texte) > 0
    resultat = ""
    for i in range(len(texte)-1):
        resultat += texte[i]
    return resultat


memoire = {}


def plus_longue_sous_chaine(texte1, texte2):
    if len(texte1) == 0 or len(texte2) == 0:
        return ""

    if (texte1, texte2) in memoire:
        return memoire[(texte1, texte2)]

    if texte1[-1] == texte2[-1]:
        memoire[(texte1, texte2)] = plus_longue_sous_chaine(
            sans_dernier(texte1), sans_dernier(texte2)) + texte1[-1]
    else:
        cas_1 = plus_longue_sous_chaine(sans_dernier(texte1), texte2)
        cas_2 = plus_longue_sous_chaine(texte1, sans_dernier(texte2))

        if len(cas_1) >= len(cas_2):
            memoire[(texte1, texte2)] = cas_1
        else:
            memoire[(texte1, texte2)] = cas_2

    return memoire[(texte1, texte2)]


# Tests

# Fonction sans_dernier
texte = 'blabla'
assert sans_dernier(texte) == 'blabl'
assert texte == 'blabla', "le texte de départ ne doit pas être modifié"
assert sans_dernier('b') == ''
assert sans_dernier('bla'*10) == 'bla'*9+'bl'


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

# Tests supplémentaires
assert sans_dernier('eee') == 'ee'
assert sans_dernier('b'*100) == 'b'*99
texte = 'f'
assert sans_dernier(texte) == ''
assert texte == 'f', "le texte de départ ne doit pas être modifié"
texte1 = "bertrand roule en vélo"
texte2 = "bravo"
assert plus_longue_sous_chaine(texte1, texte2) == 'bravo'
texte1 = "resulta"
texte2 = "résultats"
assert plus_longue_sous_chaine(texte1, texte2) == 'rsulta'
texte1 = "résultats"
texte2 = "résultats"
assert plus_longue_sous_chaine(texte1, texte2) == 'résultats'
