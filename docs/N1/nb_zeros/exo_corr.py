def nb_zeros(n):
    assert n > 0

    resultat = 0
    while n % 10 == 0:
        n = n // 10
        resultat += 1
    return resultat


# text = f"""
# for n in range(1, 123):
#     attendu = nb_zeros(n)
#     assert nb_zeros(n) == attendu, f"Erreur avec n = \{n\}"
# """

# if "for" in text:
#     print(text.split("\n"))


# # for base in [2**1000, 3**1000, 5**1000, 7**1000]:
# #     for attendu in range(10):
# #         n = base * 10**attendu
# #         assert nb_zeros(n) == attendu, f"Erreur avec n = {n}"

