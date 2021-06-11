import random

L = [random.randint(1,100) for i in range(100)]

def sommation(T: list) -> float:
    somme = 0
    for nombre in L:
        somme = somme+nombre
    return somme

print(sommation(L))