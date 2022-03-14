def sans_dernier(texte):
    assert len(texte) > 0
    """
    resultat = ""
    for i in range(len(texte)-1) :
        resultat += texte[i]
    return resultat
    """
    return texte[:-1]


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


def differences(texte, diffs):
    resultat = []
    rang_diffs = 0
    for caractere in texte:
        if rang_diffs < len(diffs) and caractere == diffs[rang_diffs]:
            resultat.append(caractere)
            rang_diffs += 1
        else:
            resultat.append("_")

    return "".join(resultat)


memoire = {}
# texte1 = "merssi de respecté l'ortaugrafe"
# texte2 = "Merci de respecter l'orthographe"
# texte1 = "lapin"
# texte2 = "caprin"
texte1 = "aaabbbbaa"
texte2 = "aaaaa"

diffs = plus_longue_sous_chaine(texte1, texte2)
print(diffs)
print(texte1)
print(differences(texte1, diffs))
print(differences(texte2, diffs))
print(texte2)
print(memoire)
# Tests
assert sans_dernier('blabla') == 'blabl'
assert sans_dernier('b') == ''
assert sans_dernier('bla'*10) == 'bla'*9+'bl'
