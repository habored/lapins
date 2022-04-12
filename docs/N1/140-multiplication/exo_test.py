from itertools import product

# Tests
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(3, -4) == -12
assert multiplication(-2, 0) == 0

# Tests supplémentaires

premiers = [a for a in range(-10, 11)]
seconds = [a for a in range(-10, 11)]
for a, b in product(premiers, seconds):
    assert multiplication(a, b) == a*b, f"Erreur sur le produit {a}*{b}"


class Entier(int):
    def __mul__(self, valeur):
        raise Exception(
            f"Vous avez utilisé la multiplication... C'est explicitement interdit !")

    def __float__(self, /):
        raise Exception(
            f"Vous avez essayé de convertir le nombre en un 'float'... Pourquoi ?")

    def __int__(self, /):
        raise Exception(
            f"Vous avez essayé de convertir le nombre en un 'int'... Pourquoi ?")


    def __pow__(self, valeur, mod=None, /):
        raise Exception(
            f"Vous avez utilisé la puissance...  qui est une multiplication !")

    def __rmul__(self, valeur, /):
        raise Exception(
            f"Vous avez utilisé la multiplication... C'est explicitement interdit !")

    def __rpow__(self, value, mod=None, /):
        raise Exception(
            f"Vous avez utilisé la puissance... qui est une multiplication !")

    def __str__(self, /):
        raise Exception(
            f"Vous avez essayé de convertir le nombre en 'str'... Pourquoi ?")


assert multiplication(Entier(2), Entier(3)) == 6
