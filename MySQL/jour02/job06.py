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

# Exécuter la requête pour récupérer la somme de la superficie de tous les étages
requete = "SELECT SUM(capacite) FROM salle"
curseur.execute(requete)

# Récupérer le résultat directement avec fetchone()
resultat_superficie = curseur.fetchone()[0]

# Afficher le résultat en console
print(f"La capacité de toute les salle est de : {resultat_superficie} ")

# Fermer le curseur et la connexion
curseur.close()
connexion.close()
