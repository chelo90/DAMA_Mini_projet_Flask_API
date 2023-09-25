import streamlit as st
import pandas as pd

# bibliothèque pour interroger l'API
import requests

# declaration des variables
api_url = "http://127.0.0.1:3003"
api_user = ""
api_pass = ""
api_token = ""

headers = {
    'Content-Type':'application/json',
    "Authorization": f"Basic{api_token}"}

# conception interface graphique

# Afficher du texte sur le navigateur
st.write("Bonjour, Bienvenue à la formation DAMA")
col_gche, col_dte = st.columns(2) # subdiviser l'interface en deux colonnes
# Colonne de gauche : Saisie du nom
nom_recherche = col_gche.text_input(label="Client à rechercher") # Zone de saisie du client à rechercher
# Ajout bouton
btn_recherche = col_gche.button("recherche")

# colonne de droite
code_client = col_dte.text_input(label="Code Client") # zone de saisie du code client
nom_client = col_dte.text_input(label="Nom Client") # zone de saisie du nom client
solde_client = col_dte.number_input(label="Solde initial", min_value=0.0) # zone de saisie du solde client
etat_client = col_dte.selectbox(
    'Etat client',
    ['Actif', 'Inactif']
)
btn_nouveau = col_dte.button("Nouveau")

# ecouteur du click
if btn_recherche:
    # 0- test de la zone de recherche
    if nom_recherche == "":
        # 1- faire appel à l'api
        response = requests.get(api_url+"/api/getAllClient", headers = headers) #auth=(api_user, api_pass))
    else:
        # 1- faire appel à l'api
        response = requests.get(api_url+f"/api/searchByName?name={nom_recherche}")
        # 2- recuperer le resultat
    if (response.status_code == 200): # si le code de retour est 200 --> OK
        resultat = response.json()
        # 3- afficher le resultat
        liste_resultat = list(resultat["resultats"]) # transformer resultat en liste
        pd_result = pd.DataFrame(liste_resultat, columns=["Code Client", "Nom Client"]) # transformer liste en dataframe
        st.dataframe(pd_result) # afficher dataframe
        #st.write(resultat["resultats"])
    else:
        st.write(f"Error code : {response.status_code}")

if btn_nouveau:
    # ajout du nouveau client avec POST
    # 1- Constituer les variables envoyées
    data = {
        "code_client":code_client,
        "nom_client":nom_client,
        "solde_client":solde_client,
        "etat": 1 if etat_client == 'Actif'else 0
        }
    # 2- Appel de l'api avec POST et les parametres
    response = requests.post(api_url+f"/api/addClient", headers = headers, json = data)
    # 3- Recuperer le resultat
    if (response.status_code == 200): # si le code de retour est 200 --> OK
        resultat = response.json()
        st.write(resultat)
    else:
        st.write(f"Error code : {response.status_code}")
    # 4- Afficher le resultat
















