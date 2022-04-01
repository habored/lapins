def moyenne(notes_ponderees):
    cumul_points = 0.0
    cumul_coeffs = 0
    for (note, coeff) in notes_ponderees:
        cumul_points += coeff * note
        cumul_coeffs += coeff
    return cumul_points / cumul_coeffs


# tests

def sont_proches(x, y):
    "Renvoie un booléen : les nombres x et y sont-ils proches ?"
    return abs(x - y) < 10**-6

assert sont_proches(moyenne([(15.0, 2)]), 15.0)
assert sont_proches(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5)
