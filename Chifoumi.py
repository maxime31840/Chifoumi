from random import choice

def affichage():
    title = " BIENVENUE SUR CHIFOUMI ! "
    border = "*" * (len(title) + 4)
    
    print("\n" + border)
    print(f"*{title}*")
    print(border + "\n")

choix = ["pierre", "feuille", "ciseaux"]

def choix_utilisateur(nom):
    user_choice = ''
    while user_choice not in choix:
        user_choice = input(f"{nom}, choisissez pierre, feuille ou ciseaux : ").lower()
    return user_choice

def choix_ordinateur_triche(user_choice, score_joueur, score_ordinateur):
    """ L'ordinateur triche s'il est en retard de 2 points ou plus. """
    if score_ordinateur + 2 <= score_joueur:
        if user_choice == "pierre":
            return "feuille"
        elif user_choice == "feuille":
            return "ciseaux"
        elif user_choice == "ciseaux":
            return "pierre"
    else:
        return choice(choix)

def resultat(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Égalité"
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "feuille" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "feuille"):
        return "Victoire"
    else:
        return "Défaite"

def chifoumi():
    affichage()

    # Choix du mode de jeu
    while True:
        mode = input("Voulez-vous jouer contre un autre joueur (1) ou contre l'ordinateur (2) ? ")
        if mode in ["1", "2"]:
            break
        else:
            print("\nVeuillez entrer '1' ou '2'.\n")

    # Saisie des noms des joueurs
    if mode == "1":
        joueur1 = input("\nNom du joueur 1 : ")
        joueur2 = input("Nom du joueur 2 : ")
    else:
        joueur1 = input("\nVotre prénom : ")
        joueur2 = "Ordinateur"

    # Demander le nombre de points gagnants
    while True:
        try:
            points_gagnants = int(input("\nCombien de points pour gagner la partie ? "))
            if points_gagnants > 0:
                break
            else:
                print("\nVeuillez entrer un nombre positif.\n")
        except ValueError:
            print("\nVeuillez entrer un nombre valide.\n")

    print("\nLa partie commence !\n")

    score_joueur1 = 0
    score_joueur2 = 0

    while score_joueur1 < points_gagnants and score_joueur2 < points_gagnants:
        print("-" * 40)

        # Récupération des choix des joueurs
        print("Pour des raisons évidente de triche, veuillez choisir dans votre tête avant de l'écrire chacun votre tour\n")
        choix1 = choix_utilisateur(joueur1)

        if mode == "1":
            choix2 = choix_utilisateur(joueur2)
        else:
            choix2 = choix_ordinateur_triche(choix1, score_joueur1, score_joueur2)

        print(f"\n{joueur1} a choisi : {choix1}")
        print(f"{joueur2} a choisi : {choix2}\n")
        
        # Résultat du tour
        resultat_partie = resultat(choix1, choix2)

        if resultat_partie == "Victoire":
            score_joueur1 += 1
            print(f">>> {joueur1} gagne ce tour !")
        elif resultat_partie == "Défaite":
            score_joueur2 += 1
            print(f">>> {joueur2} gagne ce tour !")
        else:
            print(">>> Égalité, personne ne marque de point.")

        print(f"\nScore actuel : {joueur1} {score_joueur1} - {score_joueur2} {joueur2}\n")

    print("=" * 40)
    print("\nFIN DE LA PARTIE\n")

    if score_joueur1 == points_gagnants:
        print(f"Félicitations {joueur1} ! Vous avez remporté la partie !\n")
    else:
        print(f"{joueur2} a gagné la partie !\n")

chifoumi()
