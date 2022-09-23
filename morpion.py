from ast import While
from telnetlib import STATUS


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
    :param grille:(dico) la grille du morpion
    :param joueur :(str) 0 ou X
    :return: la nouvelle grille si le coup est valide valide, false sinon.
    """
    if coup [0] in ["A","B","C"] and 0 < int(coup[1]) <2:
        if grille [coup[0]][int(coup[1])]=="_":
            grille[coup[0]][int(coup[1])]=joueur
            return grille
    return False


def est_pleine (grille):
    """
    fonction qui renvoie True si la grille est pleine, sinon False
    :param grille:(dico) la grille du morpion
    :return:(bool) true si la grille est pleine sinon False.
    """
    for cle in grille:
        if "_" in grille [cle]:
         return False
    return True

def est_gagnante (grille):
    """ 
    fonction qui renvoie True si la grille est gagnante sinon False
    :param grille:(dico) la grille du morpion
    :return:(Bool) renvoi True si quelqu'un a gagner sinon false.
    """

    for cle in grille:
        if grille [cle][0]== grille[cle][1]==grille[cle][2] and grille[cle][0]!="_":
            return True

    for i in range(3):
        if grille ["A"][i]==grille["B"][i]==grille["C"][i] and grille[A][i]!="_":
            return True


    if grille ["A"][0]==grille["B"][1]==grille["C"][2] and grille ["A"][0]!="_":
        return True

    if grille ["A"][2]==grille ["B"][1]==grille ["C"][0] and grille ["A"][2]!="_":
        return True
    
    return False


grille={
    "A":["_","_","_"],
    "B":["_","_","_"],
    "C":["_","_","_"]
}

afficher_grille(grille)

jouer_coup ("A1", grille, "X")
afficher_grille(grille)

grille=(afficher_grille)
fin=False
joueur="X"

while not fin:
    afficher_grille()
    coup=input("Entrez votre coup+joueur")
    grille2= jouer_coup(coup,grille,joueur)

    while grille2 == False:
    coup=input("Entrez votre coup+joueur")
    grille2=jouer_coup(coup,grille,joueur)
