def amis_d_amis(reseau, membre):
    ...


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
