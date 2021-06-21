import random

def sommation(T: list) -> float:
    a = 0
    for nombre in T:
        a = a+nombre
    return a

def somme(L):
    return None if len(L)==0 else sum(L)