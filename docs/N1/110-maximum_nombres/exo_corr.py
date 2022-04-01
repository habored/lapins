def maximum(nombres):
    maxi = nombres[0]
    for x in nombres:
        if x > maxi:
            maxi = x
    return maxi


# Tests
assert maximum([98, 12, 104, 23, 131, 9]) == 131
assert maximum([-27, 24, -3, 15]) == 24

