import mysql.connector

# Paramètres de connexion à la base de données
host = 'votre_host'
user = 'votre_utilisateur'
password = 'votre_mot_de_passe'
database = 'LaPlateforme'

# Se connecter à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="za9?-U5zwD4-6#L",
    database="LaPlateforme"
)

# Créer un objet curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()



# Exécuter la requête pour récupérer les noms et capacités de la table salle
requete = f"SELECT nom, capacite FROM salle"
curseur.execute(requete)

# Récupérer tous les résultats
resultats = curseur.fetchall()

# Afficher les résultats en console
liste = [] 
for nom, capacite in resultats:
    liste.append(f"('{nom},{capacite}),")
print(liste)

# Fermer le curseur et la connexion
curseur.close()
connexion.close()