def afficher_grille (grille):
    """
    fonction qui affiche la grille
    :param grille:(dict) dictionnaire qui contient des listes
    """
    for cle in grille:
        print(grille[cle])
    print("\n")


def jouer_coup(coup,grille,joueur):
    """
    fonction qui permet de jouer un coup
    :param coup:(str)le premier caractere doit etre compris entre a et c, le deuxieme caractere doit etre compris entre 0 et 2
    :param grille:(dico) la grille sur laquelle jouer le coup
    :param joueur :(str) 0 ou X
    :return: la nouvelle grille si le coup est valide valide, false sinon.
    """
    if coup [0] in ["A","B","C"] and 0 < int(coup[1]) <2:
        if grille [coup[0]][int(coup[1])]=="_":
            grille[coup[0]][int(coup[1])]=joueur
            return grille
    return False

grille={
    "A":["_","_","_"],
    "B":["_","_","_"],
    "C":["_","_","_"]
}

afficher_grille(grille)

jouer_coup ("A1", grille, "X")
afficher_grille(grille)