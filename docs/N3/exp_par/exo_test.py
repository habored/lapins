
# tests

assert est_bien_parenthesee("(2 + 4)*7") == True
assert est_bien_parenthesee("tableau[f(i) - g(i)]") == True
assert est_bien_parenthesee(
    "#include <stdio.h> int main(){int liste[2] = {4, 2}; return (10*liste[0] + liste[1]);}"
) == True

assert est_bien_parenthesee("(une parenthèse laissée ouverte") == False
assert est_bien_parenthesee("{<(}>)") == False
assert est_bien_parenthesee("c'est trop tard ;-)") == False


# autres tests


assert est_bien_parenthesee("a(b)c") == True
assert est_bien_parenthesee("a[]b") == True
assert est_bien_parenthesee("{ }") == True
assert est_bien_parenthesee("<a>") == True
assert est_bien_parenthesee("()[]{}<>") == True
assert est_bien_parenthesee("([{<>}])") == True
assert est_bien_parenthesee("<{[([{<>}])]}>") == True
assert est_bien_parenthesee(
      "("*100 + "["*100 + "{"*100 + "<"*100
    + ">"*100 + "}"*100 + "]"*100 + ")"*100
) == True

assert est_bien_parenthesee("a(bc") == False
assert est_bien_parenthesee("a]b") == False
assert est_bien_parenthesee("} {") == False
assert est_bien_parenthesee("><a><") == False
assert est_bien_parenthesee("([)]{<}>") == False
assert est_bien_parenthesee("([{<}>)]") == False
assert est_bien_parenthesee("{<([[<{>}])]}>") == False
assert est_bien_parenthesee(
      "("*100 + "["*100 + "{"*100 + "<"*100
    + "<(>)"
    + ">"*100 + "}"*100 + "]"*100 + ")"*100
) == False


