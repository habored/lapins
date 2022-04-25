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


# Autres tests
# On change de dictionnaire
classement = {'Navok': 4, 'Dinaal': 5,
              'Alexandre': 2, 'Stephane': 3, 'Raphaël': 1}
# Dictionnaire/classement vide
assert tete_de_serie(['David', 'Rafael'], {}) == 'David'
assert classement == {'Navok': 4, 'Dinaal': 5,
                      'Alexandre': 2, 'Stephane': 3, 'Raphaël': 1}
# Tests - Que des joueurs non-classés
participants = ['Dave', 'Oliver']
assert tete_de_serie(participants, classement) == 'Dave'
assert classement == {'Navok': 4, 'Dinaal': 5,
                      'Alexandre': 2, 'Stephane': 3, 'Raphaël': 1}
# Tests - Un joueur non-classé
participants = ['Dave', 'Navok', 'Stephane']
assert tete_de_serie(participants, classement) == 'Stephane'
assert classement == {'Navok': 4, 'Dinaal': 5,
                      'Alexandre': 2, 'Stephane': 3, 'Raphaël': 1}
# Tests - Que des joueurs classés
participants = ['Navok', 'Stephane', 'Daniil', 'Raphaël']
assert tete_de_serie(participants, classement) == 'Raphaël'
assert classement == {'Navok': 4, 'Dinaal': 5,
                      'Alexandre': 2, 'Stephane': 3, 'Raphaël': 1}
