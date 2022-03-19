def nb_zeros(n):
    assert n > 0

    resultat = 0
    while n % 10 == 0:
        n = n // 10
        resultat += 1
    return resultat


# text = f"""

# tests

# assert nb_zeros(42000) == 3
# assert nb_zeros(3210) == 1
# assert nb_zeros(282475249) == 0
# assert nb_zeros(7**10000) == 0
# assert nb_zeros(7**10000 * 1000) == 3
