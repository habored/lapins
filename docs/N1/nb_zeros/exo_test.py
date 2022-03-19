# tests

assert nb_zeros(42000) == 3
assert nb_zeros(3210) == 1
assert nb_zeros(282475249) == 0
assert nb_zeros(7**10000) == 0
assert nb_zeros(7**10000 * 1000) == 3


# # autres tests

# def NB_ZEROS(n):
#     resultat = 0
#     while n % 10 == 0:
#         n = n // 10
#         resultat += 1
#     return resultat

# for n in range(1, 123):
#     attendu = NB_ZEROS(n)
#     assert nb_zeros(n) == attendu, f"Erreur avec n = {n}"

# for base in [
#     2**1000, 3**1000, 5**1000, 7**1000
# ]:
#     for attendu in range(10):
#         n = base * 10**attendu
#         assert nb_zeros(n) == attendu, f"Erreur avec n = {n}"

