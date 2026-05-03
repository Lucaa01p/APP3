import heapq
from graphe import noeuds_de


def dijkstra(graphe, depart, arrivee):
    # Trouve le chemin le plus rapide entre deux stations (en secondes)
    # Retourne (temps_total, chemin) ou (None, None) si pas de chemin
    noeuds_dep = noeuds_de(graphe, depart)
    noeuds_arr = set(noeuds_de(graphe, arrivee))

    if not noeuds_dep or not noeuds_arr:
        return None, None

    distances   = {}   # distance minimale connue pour chaque noeud
    predecesseur = {}  # d'où on vient pour arriver à ce noeud

    # File de priorité : (distance, noeud)
    file = []
    for n in noeuds_dep:
        distances[n] = 0
        heapq.heappush(file, (0, n))

    visites = set()

    while len(file) > 0:
        dist, noeud = heapq.heappop(file)

        if noeud in visites:
            continue
        visites.add(noeud)

        if noeud in noeuds_arr:
            break  # on a trouvé le chemin le plus court

        for voisin, temps in graphe.get(noeud, []):
            nouvelle_dist = dist + temps
            if nouvelle_dist < distances.get(voisin, float('inf')):
                distances[voisin] = nouvelle_dist
                predecesseur[voisin] = noeud
                heapq.heappush(file, (nouvelle_dist, voisin))

    # Trouver le meilleur noeud d'arrivée
    meilleur = min(noeuds_arr, key=lambda n: distances.get(n, float('inf')))
    if distances.get(meilleur, float('inf')) == float('inf'):
        return None, None

    # Remonter le chemin depuis l'arrivée
    chemin = []
    noeud = meilleur
    while noeud is not None:
        chemin.append(noeud)
        noeud = predecesseur.get(noeud)
    chemin.reverse()

    return distances[meilleur], chemin


def afficher_itineraire(chemin, temps_total):
    # Transforme la liste de noeuds "station::ligne" en instructions lisibles
    etapes = [n.rsplit("::", 1) for n in chemin]  # [(station, ligne), ...]

    print("\n" + "=" * 50)
    for i, (station, ligne) in enumerate(etapes):
        if i == 0:
            print(f"Monter station {station}, ligne {ligne}")
        elif i == len(etapes) - 1:
            print(f"Descendre station {station}, ligne {ligne}")
        elif station == etapes[i-1][0] and ligne != etapes[i-1][1]:
            # Même station, ligne différente = correspondance
            print(f"Correspondance station {station}, prendre la ligne {ligne}")
        else:
            print(f"Continuer station {station}")

    minutes  = temps_total // 60
    secondes = temps_total % 60
    if secondes == 0:
        print(f"\nTemps total estimé : {minutes} minutes")
    else:
        print(f"\nTemps total estimé : {minutes} minutes {secondes} secondes")
    print("=" * 50)
