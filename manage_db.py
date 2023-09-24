import mysql.connector as mc

config = {
    'host': "localhost",
    'user': 'root',
    'password': 'admin123',
    'database': 'bd_test_api'
}

# fonction qui me retourne la version de ma base de données
def getDBInfo(config):
    # creation de la requete SQL
    req = "select version()"
    # connexion execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchone()
            return {'resultats': resultats[0]}
    return {'resultats': ""}   

# fonction qui retourne les clients
def getAllClients(config):
    # requete SQL
    req = "SELECT code_client, nom_client FROM client"
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}   

# fonction qui permet de rechercher en fonction du nom du client
def findClientByName(config, name):
    # requete SQL
    req = "SELECT code_client, nom_client FROM client WHERE lower(nom_client) like %s"
    params = (name.lower(), )
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""} 

# fonction qui permet d'ajouter un nouveau client
def addNewClient(config, data): # data = {"nom_client":"pierrot", "code_client":"CL768", "solde":0.0, "etat":1}
    # requete SQL
    req = "INSERT INTO client(code_client, nom_client, solde_client, etat) \
           VALUES (%s, %s, %s, %s)"
    params = [
        (data["code_client"], data["nom_client"], data["solde_client"], data["etat"])
    ]
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.executemany(req, params)
            db.commit() # pour persister les nouvelles données en BD
            resultats = c.fetchall()
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0} 

# fonction qui permet de rechercher un client en fonction de son code
def findClientByCode(config, name):
    # requete SQL
    req = "SELECT code_client, nom_client FROM client WHERE code_client like %s"
    params = (name, )
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""} 

# fonction qui permet de rechercher un client en fonction de son solde
def findClientBySolde(config, name):
    # requete SQL
    req = "SELECT code_client, nom_client, solde_client FROM client WHERE solde_client like %s"
    params = (name, )
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""} 

# fonction qui permet de rechercher les clients actifs ou inactifs en fonction de leur état
def findClientByEtat(config, name):
    # requete SQL
    req = "SELECT code_client, nom_client, solde_client, etat FROM client WHERE etat like %s"
    params = (name, )
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}

# fonction qui permet de mettre à jour les données d'un client
def updateDataClient(config, data): # data = {"code_client":"CL768","nom_client":"pierrot","solde_client":0.0,"etat":1}
    # requete SQL pour mettre à jour les données du client
    req = "UPDATE client SET nom_client = %s, solde_client = %s, etat = %s WHERE code_client = %s"
    params = [
        (data["code_client"], data["nom_client"], data["solde_client"], data["etat"])
    ]
    # connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.executemany(req, params)
            db.commit() # pour persister les nouvelles données en BD
            resultats = c.fetchall()
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0} 

