def amis_d_amis(reseau, membre):
    resultat = []
    for ami in reseau[membre]:
        for ami_de_ami in reseau[ami]:
            if ami_de_ami != membre and ami_de_ami not in resultat:
                resultat.append(ami_de_ami)
    return resultat


# Tests
immediam = {
    "Anna": ["Billy"],
    "Billy": ["Anna", "Eroll"],
    "Carl": ["Billy"],
    "Dora": ["Gaby"],
    "Eroll": ["Billy", "Dora", "Flynn", "Gaby"],
    "Flynn": ["Gaby"],
    "Gaby": ["Eroll"],
}
assert sorted(amis_d_amis(immediam, "Billy")) == ["Dora", "Flynn", "Gaby"]
assert sorted(amis_d_amis(immediam, "Eroll")) == ["Anna", "Gaby"]
assert sorted(amis_d_amis(immediam, "Dora")) == ["Eroll"]
