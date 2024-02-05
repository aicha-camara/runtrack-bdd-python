import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="za9?-U5zwD4-6#L",
    database="job07"
)

curseur = connexion.cursor()

requete = "SELECT * FROM employe WHERE salaire > 3000"
curseur.execute(requete)

resultat = curseur.fetchall()

liste = [] 
for employe in resultat:
    id, nom, prenom, salaire, id_service = employe
    liste.append(f"('{nom}', '{prenom}', {salaire}, {id_service})")
print("les emlpoyées qui ont un salaire superieur a 3000 sont :" ,liste)

requete2 = """
SELECT employe.id, employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
FROM employe
JOIN service ON employe.id_service = service.id
"""
curseur.execute(requete2)
resultat2 = curseur.fetchall()

# Afficher les résultats de la deuxième requête
for row in resultat2:
    print(row)

curseur.close()
connexion.close()


class Employe:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user, 
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def creer_employe(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def liste_employe(self):
        requete = "SELECT * FROM employe"
        self.curseur.execute(requete)
        resultat = self.curseur.fetchall()
        return resultat

    def mettre_a_jour_employe(self, employe_id, nouveau_salaire):
        requete = "UPDATE employe SET salaire = %s WHERE id = %s"
        valeurs = (nouveau_salaire, employe_id)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_employe(self, employe_id):
        requete = "DELETE FROM employe WHERE id = %s"
        valeurs = (employe_id,)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

president = Employe("localhost", "root", "za9?-U5zwD4-6#L", "job07")

president.creer_employe("Doe", "John", 4000, 1)

resultat = president.liste_employe()
print("Liste des employés après création :")
for employe in resultat:
    print(employe)

president.mettre_a_jour_employe(1, 4500)

employes = president.liste_employe()
print(" mise à jour du salaire Betty:")
for employe in employes:
    print(employe)

president.supprimer_employe(5)

resultats_apres_suppression = president.liste_employe()
print("Liste des employés après suppression :")
for employe in resultats_apres_suppression:
    print(employe)

# Fermer la connexion à la base de données
president.fermer_connexion()
