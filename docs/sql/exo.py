#--- HDR ---#
import sqlite3

def initialisation_base_de_donnee():
    base = sqlite3.connect(":memory:")
    curseur = base.cursor()

    curseur.execute(
        """
    CREATE TABLE Ordinateur
        (nom_ordi text, salle text, marque_ordi text, modele_ordi,
        annee int, video int, PRIMARY KEY (nom_ordi ));
    """
    )
    curseur.execute(
        """
    CREATE TABLE Videoprojecteur (salle text, marque_video text,
    modele_video text, tni int)
    """
    )
    curseur.execute(
        """
    CREATE TABLE Imprimante
    (nom_imprimante text, marque_imp text, modele_imp text, nom_ordi text,
    PRIMARY KEY (nom_imprimante, nom_ordi))
    """
    )
    curseur.execute(
        """
    INSERT INTO Ordinateur (nom_ordi, salle, marque_ordi, modele_ordi,
    annee, video) VALUES
    ("Gen-24", "012", "HP", "compaq pro 6300", 2012, 1),
    ("Tech-62", "114", "Lenovo", "p300", 2015, 1),
    ("Gen-132", "223", "Dell", "Insipiron Compact", 2019, 1),
    ("Gen-133", "223", "Dell", "Insipiron Compact", 2019, 0),
    ("Gen-134", "223", "Dell", "Insipiron Compact", 2019, 0)
    """
    )
    curseur.execute(
        """
    INSERT INTO Imprimante (nom_imprimante, marque_imp, modele_imp,
    nom_ordi) VALUES
    ("imp_BTS_NB", "HP", "Laserjet pro M15w", "Tech-62"),
    ("imp_BTS_Couleur", "Canon", "Megatank Pixma G5050", "Tech-62"),
    ("imp_salle-info1", "Brother", "2360DN", "Gen-132"),
    ("imp_salle-info1", "Brother", "2360DN", "Gen-133"),
    ("imp_salle-info1", "Brother", "2360DN", "Gen-134")
    """
    )
    curseur.execute(
        """
    INSERT INTO Videoprojecteur (salle, marque_video, modele_video, tni)
    VALUES
    ("012", "Epson", "xb27", 1),
    ("114", "Sanyo", "PLV-Z3", 0),
    ("223", "Optoma", "HD143X", 0),
    ("225", "Optoma", "HD143X", 1)
    """
    )
    base.commit()
    return curseur
#--- HDR ---#


curseur = initialisation_base_de_donnee()


def execute_requete(requete: str) -> list:
    curseur.execute(requete)
    return curseur.fetchall()


requete1 = execute_requete("SELECT salle, marque_ordi FROM Ordinateur")

requete2 = execute_requete("SELECT nom_ordi, salle FROM Ordinateur WHERE video = 1")

requete3 = execute_requete(
    "SELECT * from Ordinateur WHERE annee >= 2017 ORDER BY annee ASC"
)

requete4 = execute_requete(
    """
    SELECT nom_imprimante, salle, Ordinateur.nom_ordi
    FROM Imprimante
    JOIN Ordinateur ON Imprimante.nom_ordi = Ordinateur.nom_ordi
"""
)

requete5 = execute_requete(
    """
    INSERT INTO Videoprojecteur (salle, marque_video, modele_video, tni)
    VALUES ("315", "NEC", "ME402X", 0)
"""
)

assert sorted(requete1) == [
    ("012", "HP"),
    ("114", "Lenovo"),
    ("223", "Dell"),
    ("223", "Dell"),
    ("223", "Dell"),
]
assert sorted(requete2) == [
    ("Gen-24", "012"), ("Tech-62", "114"), ("Gen-132", "223")
]
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
