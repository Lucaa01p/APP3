from graphe   import charger_reseau, construire_graphe, toutes_stations, lister_villes
from parcours import bfs, dfs, verifier_connexite
from dijkstra import dijkstra, afficher_itineraire


def choisir_ville():
    villes = lister_villes()
    noms = list(villes.keys())

    print("\nVilles disponibles :")
    for i, nom in enumerate(noms):
        print(f"  {i+1}. {nom}")

    while True:
        choix = input("Votre choix (numéro) : ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(noms):
            nom = noms[int(choix) - 1]
            return charger_reseau(villes[nom]), nom
        print("Numéro invalide, réessayez.")


def saisir_station(message, stations):
    # Cherche la station tapée, propose des suggestions si introuvable
    while True:
        saisie = input(message).strip()
        if not saisie:
            continue

        # Recherche exacte (insensible à la casse)
        for s in stations:
            if s.lower() == saisie.lower():
                return s

        # Sinon on cherche les stations qui contiennent ce mot
        suggestions = sorted(s for s in stations if saisie.lower() in s.lower())
        if len(suggestions) == 1:
            print(f"  -> {suggestions[0]}")
            return suggestions[0]
        elif len(suggestions) > 1:
            print(f"  Plusieurs résultats pour '{saisie}' :")
            for i, s in enumerate(suggestions):
                print(f"    {i+1}. {s}")
            n = input("  Entrez le numéro : ").strip()
            if n.isdigit() and 1 <= int(n) <= len(suggestions):
                return suggestions[int(n) - 1]

        print("Station introuvable, réessayez.")


def main():
    print("=" * 50)
    print("  CALCULATEUR D'ITINÉRAIRE - TRANSPORTS EN COMMUN")
    print("=" * 50)

    donnees = None
    graphe  = None
    ville   = None

    while True:
        print("\n  1. Choisir une ville")
        if donnees:
            print("  2. Calculer un itinéraire")
            print("  3. Vérifier la connexité (BFS / DFS)")
            print("  4. Voir les correspondances")
        print("  0. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "0":
            print("À bientôt !")
            break

        elif choix == "1":
            donnees, ville = choisir_ville()
            graphe = construire_graphe(donnees)
            nb = len(toutes_stations(donnees))
            print(f"\nRéseau '{ville}' chargé : {len(donnees['lignes'])} ligne(s), {nb} station(s).")

        elif choix == "2" and donnees:
            stations = toutes_stations(donnees)
            dep = saisir_station("Station de départ  : ", stations)
            arr = saisir_station("Station d'arrivée  : ", stations)

            if dep == arr:
                print("Départ et arrivée identiques !")
                continue

            temps, chemin = dijkstra(graphe, dep, arr)
            if chemin is None:
                print("Aucun itinéraire trouvé.")
            else:
                afficher_itineraire(chemin, temps)

        elif choix == "3" and donnees:
            premiere = list(donnees["lignes"].values())[0]["stations"][0]
            print(f"\nBFS depuis '{premiere}' :")
            s_bfs = bfs(graphe, premiere)
            print(f"  {len(s_bfs)} stations atteintes")

            print(f"\nDFS depuis '{premiere}' :")
            s_dfs = dfs(graphe, premiere)
            print(f"  {len(s_dfs)} stations atteintes")

            verifier_connexite(graphe, donnees)

        elif choix == "4" and donnees:
            print(f"\nCorrespondances de {ville} :")
            for c in donnees["correspondances"]:
                print(f"  {c['station']}  ->  lignes {', '.join(c['lignes'])}")

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
