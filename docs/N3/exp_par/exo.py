ouvrant = "([{<"
fermant = ")]}>"
ouverture = {f: o for o, f in zip(ouvrant, fermant)}


def est_bien_parenthesee(expression):
    ...



# tests

assert est_bien_parenthesee("(2 + 4)*7") == True
assert est_bien_parenthesee("tableau[f(i) - g(i)]") == True
assert est_bien_parenthesee(
    "#include <stdio.h> int main(){int liste[2] = {4, 2}; return (10*liste[0] + liste[1]);}"
) == True

assert est_bien_parenthesee("(une parenthèse laissée ouverte") == False
assert est_bien_parenthesee("{<(}>)") == False
assert est_bien_parenthesee("c'est trop tard ;-)") == False
