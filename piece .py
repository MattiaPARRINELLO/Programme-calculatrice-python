from random import *


def piece(nbTirage):
    nbPile = 0
    nbFace = 0
    for i in range(nbTirage):
        rando = randint(0, 1)
        if rando == 0:
            nbPile += 1
    print("Nombre de pile : ", nbPile)
    print("Nombre de face : ", nbFace)
    print("Pourcentage de pile : ", nbPile / nbTirage * 100, "%")
    print("Pourcentage de face : ", nbFace / nbTirage * 100, "%")
    return nbPile, nbFace


piece(int(input("Nombre de tirages :")))
