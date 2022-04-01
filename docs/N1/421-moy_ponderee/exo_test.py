# tests

def sont_proches(x, y):
    return abs(x - y) < 10**-6

assert sont_proches(moyenne([(15.0, 2)]), 15.0)
assert sont_proches(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5)

# autres tests

assert sont_proches(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5), "Erreur sur ce test"
assert sont_proches(moyenne([( 0.0, 1)]),  0.0), "Erreur sur ce test"
assert sont_proches(moyenne([(20.0, 1)]), 20.0), "Erreur sur ce test"
assert sont_proches(moyenne([(10.0, 5)]), 10.0), "Erreur sur ce test"

