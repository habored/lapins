def tete_de_serie(participants, classement):
    assert len(participants) > 0

    ...


# Tests - Joueurs classés
classement = {'Novak': 1, 'Daniil': 2,
              'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}
participants = ['Stefanos', 'Novak', 'Rafael']
assert tete_de_serie(participants, classement) == 'Novak'
assert classement == {'Novak': 1, 'Daniil': 2,
                      'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}

# Tests - Un joueur non-classé
participants = ['Stefanos', 'Rafael', 'David', 'Novak']
assert tete_de_serie(participants, classement) == 'Novak'
assert classement == {'Novak': 1, 'Daniil': 2,
                      'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}

# Tests - Un joueur non-classé (bis)
participants = ['David', 'Novak', 'Alexander', 'Daniil']
assert tete_de_serie(participants, classement) == 'Novak'
assert classement == {'Novak': 1, 'Daniil': 2,
                      'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}
                      
# Tests - Que des joueurs non-classés
participants = ['David', 'Olivier']
assert tete_de_serie(participants, classement) == 'David'
assert classement == {'Novak': 1, 'Daniil': 2,
                      'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}
