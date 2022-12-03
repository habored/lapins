def secret_1337_motif_carre_4(x, y, a, n):
    if n > 0:
        fig.draw(square(x, y, a))
        a /= 2
        for dx, dy in [(-a, -a), (a, -a), (-a, a), (a, a)]:
            secret_1337_motif_carre_4(x + dx, y + dy, a, n - 1)


def sont_proches(x, y):
    return abs(x - y) < 10**-9


for X, Y, A, N in [
    (0, 0, 4, 1),
    (0, 0, 4, 3),
    (0, 0, 5, 4),
    (2, 3, 4, 4),
    (0, 0, 4, 7),
]:
    fig = Figure(x_min=-4, y_min=-4, x_max=+4, y_max=+4, width=256)
    motif_carre_4(X, Y, A, N)
    psolver = sorted(fig.prog)

    fig = Figure(x_min=-4, y_min=-4, x_max=+4, y_max=+4, width=256)
    secret_1337_motif_carre_4(X, Y, A, N)
    psetter = sorted(fig.prog)

    last_a = None
    i = 0
    for (a, k, x, y), (a_, k_, x_, y_) in zip(psolver, psetter):
        if (last_a is None) or not sont_proches(a, last_a):
            i += 1
        if not sont_proches(a, a_):
            if a < a_:
                assert (
                    False
                ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_}"
            else:
                assert (
                    False
                ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il a un carré de taille {a_} en trop"
        if not (sont_proches(x, x_) and sont_proches(y, y_)):
            assert (
                False
            ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_} en ({x_}, {y_})"
    if len(psetter) > len(psolver):
        (a_, k_, x_, y_) = psetter[len(psolver)]
        assert (
            False
        ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_} en ({x_}, {y_})"

# un test sur la récursivité
# import sys

# sys.setrecursionlimit(50)

# fig = Figure()
# try:
#    motif_carre_4(X, Y, A, N)
# except RecursionError:
#    pass
# except:
#    assert False, "Votre fonction doit être récursive"
