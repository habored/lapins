dizaine, unites = 0, -1
for nombre in range(21):
    unites += 1
    if unites == 10:
        dizaine += 1
        unites = 0
    print(f"{nombre} = {dizaine} dizaine et {unites} unité(s)")
