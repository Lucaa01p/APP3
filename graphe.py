import json
import os


def charger_reseau(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        return json.load(f)


def construire_graphe(donnees):
    # Chaque noeud = "station::ligne" pour pouvoir gérer les correspondances
    graphe = {}

    # Si les connexions ne sont pas dans le fichier, on les génère depuis les lignes
    connexions = donnees["connexions"]
    if len(connexions) == 0:
        temps = donnees.get("temps_moyen", 120)
        for id_ligne, ligne in donnees["lignes"].items():
            stations = ligne["stations"]
            for i in range(len(stations) - 1):
                connexions.append({"de": stations[i],     "vers": stations[i+1], "temps": temps, "ligne": id_ligne})
                connexions.append({"de": stations[i+1],   "vers": stations[i],   "temps": temps, "ligne": id_ligne})

    # Ajout des trajets normaux sur la même ligne
    for c in connexions:
        dep = c["de"] + "::" + c["ligne"]
        arr = c["vers"] + "::" + c["ligne"]
        if dep not in graphe:
            graphe[dep] = []
        graphe[dep].append((arr, c["temps"]))

    # Ajout des correspondances (changement de ligne à la même station)
    for corresp in donnees["correspondances"]:
        station = corresp["station"]
        lignes  = corresp["lignes"]
        temps   = corresp["temps"]
        for a in lignes:
            for b in lignes:
                if a != b:
                    noeud = station + "::" + a
                    if noeud not in graphe:
                        graphe[noeud] = []
                    graphe[noeud].append((station + "::" + b, temps))

    return graphe


def noeuds_de(graphe, station):
    # Retourne tous les noeuds "station::ligne" qui correspondent à ce nom de station
    resultat = []
    for noeud in graphe:
        nom, ligne = noeud.rsplit("::", 1)
        if nom == station:
            resultat.append(noeud)
    return resultat


def toutes_stations(donnees):
    stations = set()
    for ligne in donnees["lignes"].values():
        for s in ligne["stations"]:
            stations.add(s)
    return stations


def lister_villes():
    # Cherche tous les fichiers JSON dans le dossier Données (dans le même dossier que le code)
    dossier = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Données")
    villes = {}
    for fichier in os.listdir(dossier):
        if fichier.endswith(".json"):
            chemin = os.path.join(dossier, fichier)
            with open(chemin, 'r', encoding='utf-8') as f:
                data = json.load(f)
            nom = data.get("nom", fichier.replace(".json", ""))
            villes[nom] = chemin
    return villes
