def sans_dernier(texte):
    assert len(texte) > 0
    ...


# Tests
texte = 'blabla'
assert sans_dernier(texte) == 'blabl'
assert texte == 'blabla', "le texte de départ ne doit pas être modifié"
assert sans_dernier('b') == ''
assert sans_dernier('bla'*10) == 'bla'*9+'bl'
