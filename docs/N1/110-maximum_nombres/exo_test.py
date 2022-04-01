# Tests
assert maximum([98, 12, 104, 23, 131, 9]) == 131
assert maximum([-27, 24, -3, 15]) == 24
# Tests supplémentaires
assert maximum([1, 2, 3, 4, 5]) == 5
assert maximum([5, 4, 3, 2, 1]) == 5
assert maximum([5, 5, 5]) == 5
assert abs(maximum([5.01, 5.02, 5.0]) - 5.02) < 10**-6
assert maximum([-5, -4, -3, -8, -6]) == -3
