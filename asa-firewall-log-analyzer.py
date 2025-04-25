import re  # Module pour utiliser les expressions régulières
import math  # Module pour faire des calculs mathématiques (ex. arrondi supérieur avec ceil)


# a. Fonction pour afficher le contenu d’un fichier log page par page
def afficher_log_par_page(chemin_fichier, lignes_par_page=20):
    """
    Cette fonction lit un fichier ligne par ligne et les affiche page par page,
    avec un nombre de lignes déterminé par 'lignes_par_page'.
    """
    # Ouverture du fichier avec encodage UTF-8 (ignore les erreurs s’il y a des caractères invalides)
    with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as fichier:
        lignes = fichier.readlines()  # Stocke toutes les lignes dans une liste
        total_lignes = len(lignes)  # Nombre total de lignes
        total_pages = math.ceil(total_lignes / lignes_par_page)  # Calcule le nombre total de pages

        # Affichage page par page
        for numero_page in range(total_pages):
            debut = numero_page * lignes_par_page  # Ligne de départ
            fin = debut + lignes_par_page  # Ligne de fin
            print(f"\nPage {numero_page + 1}/{total_pages} :\n")  # Numéro de page affiché
            for ligne in lignes[debut:fin]:  # Affiche chaque ligne de la page actuelle
                print(ligne.strip())  # .strip() supprime les espaces ou sauts de ligne inutiles
            if numero_page < total_pages - 1:
                input("Appuyez sur Entrée pour continuer...\n")  # Pause entre les pages


# b. Fonction pour afficher uniquement les messages d’un certain niveau de sévérité
def afficher_logs_par_severite(chemin_fichier, niveau_severite):
    """
    Cette fonction affiche uniquement les lignes de log contenant un niveau de sévérité donné (0 à 7).
    """
    with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as fichier:
        for ligne in fichier:
            # Recherche du motif %ASA-X- (X étant le niveau de sévérité)
            correspondance = re.search(r"%ASA-(\d)-", ligne)
            # Si le niveau trouvé correspond à celui demandé, on affiche la ligne
            if correspondance and int(correspondance.group(1)) == niveau_severite:
                print(ligne.strip())


# c. Fonction pour rechercher un type de message dans le fichier
def rechercher_type_message(chemin_fichier, motif_recherche):
    """
    Cette fonction affiche toutes les lignes qui contiennent une chaîne spécifique,
    par exemple 'access-list acl_in permitted'.
    """
    with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as fichier:
        for ligne in fichier:
            if motif_recherche in ligne:  # Si la chaîne est présente dans la ligne
                print(ligne.strip())


# d. Fonction pour calculer le taux de connexions refusées (Deny) par rapport aux connexions totales
def calculer_taux_connexions_refusees(chemin_fichier):
    """
    Cette fonction compte le nombre de connexions autorisées (permitted) et refusées (Deny),
    puis affiche le pourcentage de connexions refusées.
    """
    total_connexions = 0  # Nombre total de connexions (Deny + permitted)
    connexions_refusees = 0  # Nombre de connexions refusées uniquement

    with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as fichier:
        for ligne in fichier:
           
           
           
                if 'permitted' in ligne:  # Connexion autorisée
                    total_connexions += 1
                elif 'Deny' in ligne:  # Connexion refusée
                    connexions_refusees += 1
                    total_connexions += 1

    # Affichage des résultats
    if total_connexions == 0:
        print("Aucune connexion détectée.")
    else:
        print(f"Total des connexions (permitted + Deny) : {total_connexions}")
        print(f"Connexions refusées (Deny) : {connexions_refusees}")
        pourcentage = (connexions_refusees / total_connexions) * 100
        print(f"Pourcentage de connexions refusées : {pourcentage:.2f}%")


# Code principal – exécution des fonctions
if __name__ == "__main__":
    # Définition du chemin vers le fichier log
    chemin_log = r"C:/Users/lenovo/Desktop/tp5/asa-fix.log"

    # Appel de chaque fonction avec affichage des résultats
    print("\n=== a. Affichage page par page ===")
    afficher_log_par_page(chemin_log, lignes_par_page=5)

    print("\n=== b. Affichage des messages avec sévérité 4 ===")
    afficher_logs_par_severite(chemin_log, 4)

    print("\n=== c. Recherche du message 'access-list acl_in permitted' ===")
    rechercher_type_message(chemin_log, 'access-list acl_in permitted')

    print("\n=== d. Analyse des connexions refusées ===")
    calculer_taux_connexions_refusees(chemin_log)
