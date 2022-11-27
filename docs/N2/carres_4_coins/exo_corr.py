#--- HDR ---#
from js import document
class Figure():
    def __init__(self, *, x_min=None, y_min=None, x_max=None, y_max=None, width=None, height=None):
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
            self.width = round(self.height * (self.x_max - self.x_min) / (self.y_max - self.y_min))
        else:
            self.width = round(width)
            self.height = round(self.width * (self.y_max - self.y_min) / (self.x_max - self.x_min))
        

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
        ans.append(f'&ltsvg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.width}px" height="{self.height}px" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" stroke="black" >')
        if self.prog != []:
            for a, _, x, y in self.prog:
                i = _i(y+a/2)
                j = _j(x-a/2)
                r = _l(a/8)
                l = _l(a)
                e = _l(a/16)
                ans.append(
                    f'&ltrect x="{j}" y="{i}" rx="{r}" ry="{r}" width="{l}" height="{l}" stroke-width="{e}" />'
                )
        ans.append("&lt/svg>")
        return "\n".join(ans).replace("&lt", "<")
    
    def draw(self, truc):
        x, y, a = truc
        assert a > 0, "Le côté doit être strictement positif"
        self.prog.append((a, 13*x + 7*y, x, y))

    def done(self, elt_id="fig_geometry"):
        elt = document.getElementById(elt_id)
        elt.innerHTML = self._repr_svg_()

def square(x, y, a):
    return (x, y, a)
#--- HDR ---#
def motif_carre_4(x, y, a, n):
    if n > 0:
        fig.draw(square(x, y, a))
        b = a / 2
        for dx, dy in [(-b, -b), (b, -b), (-b, b), (b, b)]:
            motif_carre_4(x + dx, y + dy, b, n - 1)

fig = Figure(x_min=-4, y_min=-4, x_max=+4, y_max=+4, width=256)

motif_carre_4(0, 0, 4, 4)

fig.done()
