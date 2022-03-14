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