# Tests
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tab2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
tab3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
assert redimensionner(tab1, 6, 2) == tab2
assert redimensionner(tab1, 3, 4) == tab3

# Tests supplémentaires
tab4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
assert redimensionner(tab1, 12, 1) == tab4
tab5 = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
assert redimensionner(tab1, 1, 12) == tab5
tab6 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
assert redimensionner(tab1, 2, 6) == tab6
tab10_2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
]
tab5_4 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
assert redimensionner(tab10_2, 5, 4) == tab5_4
