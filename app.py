# import des bibliotheques flask
from flask import Flask, request, json, jsonify

from manage_lib import *
from manage_db import *

# création de l'application REST
app = Flask(__name__)

# route ou endpoint
@app.route("/api/Bonjour")
def bonjour():
    msg = direBonjour()
    return msg
 
# route qui permet de dire bonjour avec un prenom
# appel : http://192.168.1.64:3003/api/bonjourPrenom?prenom=pierre&nom=paul
@app.route("/api/bonjourPrenom", methods = ['GET'])
def bonjourPrenom():
     # recuperer la donnée dans l'url
     data_prenom = request.args.get("prenom", default="", type=str)
     data_nom = request.args.get("nom", default="", type=str)

     # appel de fonction
     msg = direBonjourprenom(prenom=data_prenom, nom=data_nom)

     # retourne un résultat
     return msg

# Route pour Info DB
# appel http://192.168.1.64:3003/api/infoDB
@app.route("/api/infoDB", methods = ['GET'])
def infoDB(): 
    val = getDBInfo(config = config)
    return jsonify(val)

# Route pour tous les clients
# appel http://192.168.1.64:3003/api/getAllClient
@app.route("/api/getAllClient", methods = ['GET'])
def getAllClient(): 
    val = getAllClients(config = config)
    return jsonify(val)

# Route pour rechercher un client par nom
# appel http://192.168.1.64:3003/api/searchByName?name=pierre
@app.route("/api/searchByName", methods = ['GET'])
def searchByName(): 
    name = request.args.get("name", default = "", type = str)
    val = findClientByName(config=config, name=name)
    return jsonify(val)

# Route pour ajouter un nouveau client
# 1- methode: POST
# 2- parametres: code_client, nom_client, solde_client, etat
# 3- route: /api/addClient
# appel: ???
@app.route("/api/addClient", methods = ['POST'])
def addClient(): # methode appelée lors de l'appel de la route http://192.168.93.188:3003/api/addClient
    # recupere les données envoyées par le client (parametres)
    # données = {"code_client":"CL768","nom_client":"pierrot","solde_client":0.0,"etat":1}
    donnees = json.loads(request.data)
    # Appel de fonction pour ajout d'un nouveau client
    val = addNewClient(config = config, data = donnees)
    # retourne un résultat
    return jsonify(val)

# Route pour rechercher un client selon son code
# appel http://192.168.1.64:3003/api/searchByCode?name=CL650
@app.route("/api/searchByCode", methods = ['GET'])
def searchByCode(): 
    name = request.args.get("name", default = "", type = str)
    val = findClientByCode(config=config, name=name)
    return jsonify(val)

# Route pour rechercher un client selon son solde
# appel http://192.168.1.64:3003/api/searchBySolde?name=2000000
@app.route("/api/searchBySolde", methods = ['GET'])
def searchBySolde(): 
    name = request.args.get("name", default = "", type = str)
    val = findClientBySolde(config=config, name=name)
    return jsonify(val)

# Route pour rechercher les clients actifs ou inactifs selon leur état
# appel http://192.168.1.64:3003/api/searchByEtat?name=1
@app.route("/api/searchByEtat", methods = ['GET'])
def searchByEtat(): 
    name = request.args.get("name", default = "", type = str)
    val = findClientByEtat(config=config, name=name)
    return jsonify(val)

# Route pour mettre à jour les données d'un client
# 1- methode: POST
# 2- parametres: code_client, nom_client, solde_client, etat
# 3- route: /api/updateClient
# appel: ???
@app.route("/api/updateClient", methods = ['POST'])
def updateClient(): # methode appelée lors de l'appel de la route http://192.168.93.188:3003/api/updateClient
    # Récupérer les données JSON envoyées dans la requête
    data = json.loads(request.data)

    # Vérifier si le champ 'code_client' existe dans les données reçues
    if 'code_client' in data:
        code_client = data['code_client']

        # Vous avez maintenant le code_client saisi dans le champ de recherche.
        # Vous pouvez utiliser ce code_client pour mettre à jour les données du client en conséquence.
        # Par exemple, vous pouvez rechercher le client dans la base de données en utilisant le code_client
        # et mettre à jour les autres champs (nom_client, solde_client, etat) en fonction des données reçues.

        # Appel de la fonction pour mettre à jour les données du client
        val = updateDataClient(config=config, data=data)

        # Retourner un résultat
        return jsonify(val)
    else:
        # Si le champ 'code_client' n'est pas présent dans les données, renvoyer une réponse d'erreur
        return jsonify({'error': 'Le champ "code_client" est manquant, veuillez le saisir.'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003, debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            










































