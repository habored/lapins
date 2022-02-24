assert sorted(requete1) == [
    ("012", "HP"),
    ("114", "Lenovo"),
    ("223", "Dell"),
    ("223", "Dell"),
    ("223", "Dell"),
]
assert sorted(requete2) == [("Gen-24", "012"), ("Tech-62", "114"), ("Gen-132", "223")]
assert sorted(requete3) == [
    ("Gen-132", "223", "Dell", "Insipiron Compact", 2019, 1),
    ("Gen-133", "223", "Dell", "Insipiron Compact", 2019, 0),
    ("Gen-134", "223", "Dell", "Insipiron Compact", 2019, 0),
]
assert sorted(requete4) == [
    ("imp_BTS_Couleur", "114", "Tech-62"),
    ("imp_BTS_NB", "114", "Tech-62"),
    ("imp_salle-info1", "223", "Gen-132"),
    ("imp_salle-info1", "223", "Gen-133"),
    ("imp_salle-info1", "223", "Gen-134"),
]
assert execute_requete("SELECT * FROM Videoprojecteur WHERE salle = '315'") == [
    ("315", "NEC", "ME402X", 0)
]
