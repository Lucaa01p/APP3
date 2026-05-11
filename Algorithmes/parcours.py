from graphe import noeuds_de, toutes_stations


def bfs(graphe, station_depart):
    # Parcours en largeur : explore niveau par niveau (file FIFO)
    # Retourne toutes les stations accessibles depuis station_depart
    file = noeuds_de(graphe, station_depart)
    visites = set(file)

    while len(file) > 0:
        noeud = file.pop(0)  # on prend le premier
        for voisin, temps in graphe.get(noeud, []):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)

    # On enlève le suffixe "::ligne" pour ne garder que les noms
    return set(n.rsplit("::", 1)[0] for n in visites)


def dfs(graphe, station_depart):
    # Parcours en profondeur : explore jusqu'au bout avant de revenir (pile LIFO)
    # Retourne toutes les stations accessibles depuis station_depart
    pile = noeuds_de(graphe, station_depart)
    visites = set(pile)

    while len(pile) > 0:
        noeud = pile.pop()  # on prend le dernier
        for voisin, temps in graphe.get(noeud, []):
            if voisin not in visites:
                visites.add(voisin)
                pile.append(voisin)

    return set(n.rsplit("::", 1)[0] for n in visites)


def verifier_connexite(graphe, donnees):
    toutes = toutes_stations(donnees)
    # On part de la première station de la première ligne
    depart = list(donnees["lignes"].values())[0]["stations"][0]

    atteintes = bfs(graphe, depart)
    manquantes = toutes - atteintes

    if len(manquantes) == 0:
        print(f"Réseau connexe : toutes les {len(toutes)} stations sont accessibles.")
    else:
        print(f"ATTENTION : {len(manquantes)} station(s) inaccessible(s) !")
        for s in list(manquantes)[:5]:
            print(f"  - {s}")
