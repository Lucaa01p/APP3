# APP3
README - APP 3 Membres du groupe et rôles: Nguyen Hoang : Activateur, intégrateur Git Pillot Luca : Circulateur de parole, scribe Marniquet Lou : Barreur, secrétaire Sraka Clément : Faiseur de point, Testeur Megel Matthieu : Gardien du temps

1. Description Ce projet consiste à concevoir un calculateur d'itinéraires pour differents moyens de transports (métro, tramway, bus) capable de fonctionner entièrement hors ligne. L'objectif est de permettre aux étudiants de l'ESME de naviguer efficacement dans les réseaux de transport des métropoles où l'école est située: Paris, Lyon, Lille et Bordeaux. Le moteur de calcul repose sur la théorie des graphes. Le programme doit charger des données urbaines complexes via des fichiers JSON et déterminer le trajet optimal en termes de temps de parcours, en prenant en compte les correspondances et perturbations (fermetures de stations ou de lignes).

2. Structure du projet Afin de garantir un code modulaire et générique, la structure suivante est adoptée : main.py : Point d'entrée. Gère le menu interactif en console et la navigation utilisateur. graph_engine.py : Contient la logique de construction du graphe (matrice ou liste d'adjacence) et les algorithmes fondamentaux. algorithms.py : Implémentation des algorithmes de parcours (BFS, DFS) et de recherche du plus court chemin (Dijkstra). data_loader.py : Gère la lecture et le parsing des fichiers JSON des différentes villes. data/ : Dossier contenant les fichiers de données JSON pour Paris, Bordeaux, Lille et Lyon. rapport_APP3.pdf : Rapport synthétique expliquant les choix de structures de données, la gestion de la généricité et les solutions aux problèmes rencontrés.

3. Plan d'action (Code à faire) Étape 1 : Chargement et Modélisation Implémenter le chargeur de données JSON (Lignes, Connexions, Correspondances). Construire le graphe pondéré en choisissant la structure la plus adaptée (Liste d'adjacence recommandée pour la densité du réseau). Développer une fonction de vérification de l'accessibilité du réseau (connectivité).

Étape 2 : Algorithmes de Parcours Implémenter le parcours en largeur (BFS) pour trouver le trajet avec le moins d'arrêts. Implémenter le parcours en profondeur (DFS). Identifier et lister automatiquement les stations de correspondance.

Étape 3 : Optimisation du Trajet (Cœur du projet) Développer l'algorithme de Dijkstra pour minimiser le temps de parcours. Contrainte métier : Intégrer un coût fixe de 120 secondes pour chaque correspondance effectuée. Créer une fonction de reconstruction du chemin pour afficher l'itinéraire étape par étape.

Étape 4 : Généralisation et Interface Assurer la généricité : changer de ville doit se faire sans modifier le code source. Créer l'interface console : sélection de ville, saisie sécurisée des stations, et affichage clair du temps total.

4. Finalisation et Gestion des Aléas Gestion des perturbations : Permettre de recalculer un trajet en excluant une station ou une ligne fermée. Comparer les performances (temps normal vs temps perturbé). Produire le rapport final sur les objectifs d'app
