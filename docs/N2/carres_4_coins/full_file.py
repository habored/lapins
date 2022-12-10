# --- HDR ---#
class Figure:
    def __init__(
        self, *, x_min=None, y_min=None, x_max=None, y_max=None, width=None, height=None
    ):
        """x_min, y_min, x_max **et** y_max en paramètres nommés obligatoires
        width **ou** height en paramètres nommés obligatoires
        """
        assert x_min is not None, "Il faut préciser x_min"
        assert x_max is not None, "Il faut préciser x_max"
        assert y_min is not None, "Il faut préciser y_min"
        assert y_max is not None, "Il faut préciser y_max"
        self.x_min = float(x_min)
        self.x_max = float(x_max)
        self.y_min = float(y_min)
        self.y_max = float(y_max)
        assert self.x_min < self.x_max
        assert self.y_min < self.y_max

        if width is None:
            assert height is not None, "Il faut préciser soit width, soit height"
            self.height = round(height)
            self.width = round(
                self.height * (self.x_max - self.x_min) / (self.y_max - self.y_min)
            )
        else:
            self.width = round(width)
            self.height = round(
                self.width * (self.y_max - self.y_min) / (self.x_max - self.x_min)
            )

        self.prog = []

    def _repr_svg_(self):
        BASE = 2**20  # 1048576
        if self.width < self.height:
            WIDTH = BASE  # coordonnées
            HEIGHT = BASE * self.height // self.width
            k = HEIGHT / (self.y_max - self.y_min)
        else:
            HEIGHT = BASE  # coordonnées
            WIDTH = BASE * self.width // self.height
            k = WIDTH / (self.x_max - self.x_min)

        def _j(x):
            j = round((x - self.x_min) * k)
            return j

        def _i(y):
            i = round((self.y_max - y) * k)
            return i

        def _l(a):
            return round(a * k)

        ans = ['&lt?xml version="1.0" encoding="UTF-8"?>']
        ans.append(
            f'&ltsvg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.width}px" height="{self.height}px" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" stroke="black" >'
        )
        if self.prog != []:
            for a, _, x, y in self.prog:
                i = _i(y + a / 2)
                j = _j(x - a / 2)
                r = _l(a / 8)
                l = _l(a)
                e = _l(a / 16)
                ans.append(
                    f'&ltrect x="{j}" y="{i}" rx="{r}" ry="{r}" width="{l}" height="{l}" stroke-width="{e}" />'
                )
        ans.append("&lt/svg>")
        return "\n".join(ans).replace("&lt", "<")

    def draw(self, truc):
        x, y, a = truc
        assert a > 0, "Le côté doit être strictement positif"
        self.prog.append((a, 13 * x + 7 * y, x, y))


def square(x, y, a):
    return (x, y, a)


# --- HDR ---#
def motif_carre_4(x, y, a, n):
    if n > 0:
        fig.draw(square(x, y, a))
        b = a / 2
        for dx, dy in [(-b, -b), (b, -b), (-b, b), (b, b)]:
            motif_carre_4(x + dx, y + dy, b, n - 1)


def secret_1337_motif_carre_4(x, y, a, n):
    if n > 0:
        fig.draw(square(x, y, a))
        a /= 2
        for dx, dy in [(-a, -a), (a, -a), (-a, a), (a, a)]:
            motif_carre_4(x + dx, y + dy, a, n - 1)


def sont_proches(x, y):
    return abs(x - y) < 10**-9


X, Y, A, N = 0, 0, 4, 1

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


# for X, Y, A, N in [
#     (0, 0, 4, 1),
#     (0, 0, 4, 3),
#     (0, 0, 5, 4),
#     (2, 3, 4, 4),
#     (0, 0, 4, 7),
# ]:
#     fig = Figure()
#     motif_carre_4(X, Y, A, N)
#     psolver = sorted(fig.prog)

#     fig = Figure()
#     secret_1337_motif_carre_4(X, Y, A, N)
#     psetter = sorted(fig.prog)

#     last_a = None
#     i = 0
#     for (a, k, x, y), (a_, k_, x_, y_) in zip(psolver, psetter):
#         if (last_a is None) or not sont_proches(a, last_a):
#             i += 1
#         if not sont_proches(a, a_):
#             if a < a_:
#                 assert (
#                     False
#                 ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_}"
#             else:
#                 assert (
#                     False
#                 ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il a un carré de taille {a_} en trop"
#         if not (sont_proches(x, x_) and sont_proches(y, y_)):
#             assert (
#                 False
#             ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_} en ({x_}, {y_})"
#     if len(psetter) > len(psolver):
#         (a_, k_, x_, y_) = psetter[len(psolver)]
#         assert (
#             False
#         ), f"Pour (x, y, a, n) = {(X, Y, A, N)}, il manque un carré de taille {a_} en ({x_}, {y_})"

# un test sur la récursivité
# import sys
# sys.setrecursionlimit(5)

# fig = Figure()
# try:
#     motif_carre_4(X, Y, A, N)
# except RecursionError:
#     pass
# except:
#     assert False, "Votre fonction doit être récursive"
