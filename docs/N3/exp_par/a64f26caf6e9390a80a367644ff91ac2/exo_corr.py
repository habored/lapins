ouvrant = "([{<"
fermant = ")]}>"
ouverture = {f: o for o, f in zip(ouvrant, fermant)}

def est_bien_parenthesee(expression):
    pile = []
    for c in expression:
        if c in ouvrant:
            pile.append(c)
        elif c in fermant:
            if pile == [] or pile.pop() != ouverture[c]:
                return False
    return pile == []




# tests

assert est_bien_parenthesee("(2 + 4)*7") == True
assert est_bien_parenthesee("tableau[f(i) - g(i)]") == True
assert est_bien_parenthesee("(une parenthèse laissée ouverte") == False
assert est_bien_parenthesee("{<(}>)") == False
assert est_bien_parenthesee("c'est trop tard ;-)") == False
