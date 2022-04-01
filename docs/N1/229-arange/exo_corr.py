def arange(a, b, pas):
    resultat = []
    x = a
    while x < b - 10**-6:
        resultat.append(x)
        x += pas
    return resultat


# tests

EPS = 10**-6
def sont_proches(x, y):
    return abs(x - y) < EPS

resultat = arange(2.0, 4.0, 0.5)
attendu = [2.0, 2.5, 3.0, 3.5]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for x, y in zip(resultat, attendu):
    assert sont_proches(x, y), f"Erreur avec {x} qui n'est pas proche de {y} dans arange(2.0, 4.0, 0.5)"

resultat = arange(5.0, 6.5, 0.25)
attendu = [5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for x, y in zip(resultat, attendu):
    assert sont_proches(x, y), f"Erreur avec {x} qui n'est pas proche de {y} dans arange(5.0, 6.5, 0.25)"
