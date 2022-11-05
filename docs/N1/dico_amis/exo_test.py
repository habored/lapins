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


# Tests supplémentaires
immediam = {
    "Anna": ["Billy"],
    "Billy": ["Anna"],
    "Carl": ["Billy"],
    "Dora": ["Gaby"],
    "Eroll": ["Billy", "Dora", "Flynn", "Gaby"],
    "Flynn": ["Eroll", "Gaby"],
    "Gaby": ["Eroll", "Flynn"],
    "Charles": [],
}

assert amis_d_amis(immediam, "Anna") == []
assert sorted(amis_d_amis(immediam, "Gaby")) == ["Billy", "Dora", "Eroll", "Flynn"]
assert amis_d_amis(immediam, "Charles") == []
