import math

def def_c(r):
    def def_h(h):
        return r ** 2 * math.pi * h
    return def_h

r = def_c(5)
pl = r(10)
print(pl)




