from math import *
from time import sleep
# Infomrations sur le programme
#   Canal : Beta
#   Dernière mise a jour : 06/04/2023
#   Version : 2.3.0
#   Auteur : Mattia PARRINELLO
#   Informations :
#      - Le canal public n'est mis a jour que lorsque nous seront à la version 2.5.0 BETA ce qui donne la version 2.0.0 PUBLIC
#   Nouveautés de la mise a jour 2.2.0 :
#      - Ajout du calcul de déterminant
#      - Ajout d'un patch note pour toutes les futures versions
#   Nouveautés de la mise a jour 2.3.0 :
#      - Ajout d'un système de verification si coolinéaire ou non'
v = "2.3.0"
dateVersion = "06/04/2023"
branch = "Beta"
version = "Version : ", v


def informations():
    print("Informations sur le programme :")
    print("   Canal de publication : ", branch)
    print("   Dernière mise a jour : ", dateVersion)
    print("   Version : ", v)
    print("   Auteur : Mattia PARRINELLO")
    print("   Nouveautés de la mise a jour 2.2.0 :")
    print("      - Ajout du calcul de déterminant")
    print("      - Ajout d'un patch note pour toutes les futures versions")
    print("   Nouveautés de la mise a jour 2.3.0 :")
    print("      - Ajout d'un système de verification si coolinéaire ou non")
    sleep(10)
    home(1)


version = "Version 2.2.0"


def clear(n):
    print("\n"*n)


def home(p):
    if p == 1:
        print(version)
        sleep(1)
        clear(3)
        print("        _______________ ")
        print("       |               |")
        print("       |   PROGRAMME   |")
        print("       |    PAGE N1    |")
        print("       |_______________|")
        clear(0)
        print("1.  Distance plan")
        print("2.  Allignement")
        print("3.  Pythagore")
        print("4.  Conversion note")
        print("5.  Page Suivante")
        clear(0)
        choix = input("Indiquer votre choix : ")
        ch(choix, p)
    elif p == 2:
        print(version)
        clear(3)
        print("        _______________ ")
        print("       |               |")
        print("       |   PROGRAMME   |")
        print("       |    PAGE N2    |")
        print("       |_______________|")
        clear(0)
        print("6.  Puissance Infferieure")
        print("7.  Puissance Superieure")
        print("8.  Nombre premier")
        print("9.  Page Suivante")
        print("10. Page Precedente")
        clear(0)
        choix = input("Indiquer votre choix : ")
        ch(choix, p)
    elif p == 3:
        print(version)
        clear(3)
        print("        _______________ ")
        print("       |               |")
        print("       |   PROGRAMME   |")
        print("       |    PAGE N3    |")
        print("       |_______________|")
        clear(0)
        print("11. Puissance de 10")
        print("12. Moyenne")
        print("13. % -> CM")
        print("14. Page Suivante")
        print("15. Page Precedente")
        clear(0)
        choix = input("Indiquer votre choix : ")
        ch(choix, p)
    elif p == 4:
        print(version)
        clear(3)
        print("        _______________ ")
        print("       |               |")
        print("       |   PROGRAMME   |")
        print("       |    PAGE N4    |")
        print("       |_______________|")
        clear(0)
        print("16. CM -> %")
        print("17. CM cumulé")
        print("18. Calculer déterminant")
        print("19. Page Suivante")
        print("20. Page Precedente")
        clear(0)
        choix = input("Indiquer votre choix : ")
        ch(choix, p)
    elif p == 5:
        print(version)
        clear(3)
        print("        _______________ ")
        print("       |               |")
        print("       |   PROGRAMME   |")
        print("       |    PAGE N5    |")
        print("       |_______________|")
        clear(0)
        print("21. Coolinéaire ?")
        print("22. A venir")
        print("23. A venir")
        print("24. A venir")
        print("25. Page Precedente")


def ch(choix, p):
    clear(10)
    if choix.isdigit() == False:
        print("Erreur")
        sleep(1)
        home(p)
    else:
        choix = int(choix)
    if choix == 0:
        informations()
    # Changement page################################
    elif choix == 5 or choix == 9 or choix == 14 or choix == 19:
        home(p+1)
    elif choix == 10 or choix == 15 or choix == 20 or choix == 25:
        home(p-1)
    #################################################
    elif choix == 1:
        distance()
    elif choix == 2:
        allignement()
    elif choix == 3:
        pythagore()
    elif choix == 4:
        note()
    elif choix == 5 or choix == 9 or choix == 14:
        home(p+1)
    elif choix == 10 or choix == 15 or choix == 20:
        home(p-1)
    elif choix == 6:
        puissance_inf()
    elif choix == 7:
        puissance_sup()
    elif choix == 8:
        nb_premier()
    elif choix == 11:
        puissance_10()
    elif choix == 12:
        moyenne()
    elif choix == 13:
        pourcentage_CM()
    elif choix == 16:
        CM_pourcentage()
    elif choix == 17:
        CM_cumule()
    elif choix == 18:
        determinant()
    elif choix == 21:
        isColinear()
    else:
        print("Erreur")
        sleep(1)
        home(p)


def distance():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |   DISTANCE    |")
    print("       |_______________|")
    clear(0)
    xA = float(input("Indiquer la valeur de xA : "))
    xB = float(input("Indiquer la valeur de xB : "))
    yA = float(input("Indiquer la valeur de yA : "))
    yB = float(input("Indiquer la valeur de yB : "))
    result(sqrt((xA - xB)**2 + (yA - yB)**2))


def allignement():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  ALLIGNEMENT  |")
    print("       |_______________|")
    clear(0)
    xA = float(input("Indiquer la valeur de xA : "))
    xB = float(input("Indiquer la valeur de xB : "))
    xC = float(input("Indiquer la valeur de xC : "))
    yA = float(input("Indiquer la valeur de yA : "))
    yB = float(input("Indiquer la valeur de yB : "))
    yC = float(input("Indiquer la valeur de yC : "))
    d1 = sqrt((xA - yA)**2 + (xB - yB)**2)
    d2 = sqrt((xB - yB)**2 + (xC - yC)**2)
    d3 = sqrt((xA - yA)**2 + (xC - yC)**2)
    result(d1 + d2 == d3 or d1 + d3 == d2 or d2 + d3 == d1)


def pythagore():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |   PYTHAGORE   |")
    print("       |_______________|")
    clear(0)
    a = float(input("Indiquer la valeur de a : "))
    b = float(input("Indiquer la valeur de b : "))
    result(sqrt(a**2 + b**2))


def note():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  CALCUL NOTE  |")
    print("       |_______________|")
    clear(0)
    sur = float(input("Indiquer la valeur \nde la note sur : "))
    note = float(input("Indiquer la valeur \nde la note : "))
    finalite = float(input("Indiquer la valeur \nde la note finale : "))
    result((finalite * note)/sur)


def puissance_inf():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  PUISSANCE <  |")
    print("       |_______________|")
    clear(0)
    n = float(input("Indiquer le résultat \nvoulu : "))
    x = float(input("Indiquer la puissance \nvoulu : "))
    y = 0
    while x**y < n:
        y += 1
    result(y-1)


def puissance_sup():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  PUISSANCE >  |")
    print("       |_______________|")
    clear(0)
    n = float(input("Indiquer le résultat \nvoulu : "))
    x = float(input("Indiquer la puissance \nvoulu : "))
    y = 0
    while x**y < n:
        y += 1
    result(y)


def nb_premier():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  NB PREMIERS  |")
    print("       |_______________|")
    clear(0)
    n = float(input("Indiquer le nombre : "))
    prime_flag = 0
    if (n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            result(True)
        else:
            result(False)
    else:
        result(False)


def puissance_10():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       | PUISSANCES 10 |")
    print("       |_______________|")
    clear(0)
    n = float(input("Indiquer le nombre : "))
    if n == 0:
        return 0, 0
    neg = n < 0
    if neg:
        n = -n
    a = 1.0 * n / 10**(floor(log10(n)))
    b = int(floor(log10(n)))
    if neg:
        a = -a
    r = a, b
    result(r)


def moyenne():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |    MOYENNE    |")
    print("       |_______________|")
    clear(0)
    nbr = int(input("Indiquer le nombre \nde notes : "))
    i = 1
    notes = []
    totalNotes = []
    while i <= nbr:
        note = float(input("Indiquer la note : "))
        sur = float(input("Indiquer sur combien \nest la note : "))
        coeficient = float(input("Indiquer le \ncoeficient : "))
        if sur != 20:
            note = (note * 20)/sur
        notes.append(note*coeficient)
        totalNotes.append(coeficient)
        i += 1
    result(sum(notes)/sum(totalNotes))


def pourcentage_CM():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |    % -> CM    |")
    print("       |_______________|")
    clear(0)
    pr = float(input("Indiquer le pourcentage : "))
    result((pr/100)+1)


def CM_pourcentage():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |    CM -> %    |")
    print("       |_______________|")
    clear(0)
    cm = float(input("Indiquer le \ncoeficient multiplicateur : "))
    result((cm-1)*100)


def CM_cumule():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |   CM CUMULE   |")
    print("       |_______________|")
    clear(0)
    cm = float(input("Indiquer le \ncoeficient multiplicateur : "))
    cm2 = float(input("Indiquer le \ncoeficient multiplicateur : "))
    result(cm*cm2)


def determinant():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  DETERMINANT  |")
    print("       |_______________|")
    clear(0)
    x1, y1 = map(float, input(
        "Entrez les coordonnées du premier vecteur (séparées par une virgule) : ").split(','))

    x2, y2 = map(float, input(
        "Entrez les coordonnées du deuxième vecteur (séparées par une virgule) : ").split(','))
    result(x1 * y2 - x2 * y1)


def isColinear():
    print("        _______________ ")
    print("       |               |")
    print("       |   PROGRAMME   |")
    print("       |  COLINEAIRE   |")
    print("       |_______________|")
    clear(0)
    x1, y1 = map(float, input(
        "Entrez les coordonnées du premier vecteur (séparées par une virgule) : ").split(','))
    x2, y2 = map(float, input(
        "Entrez les coordonnées du deuxième vecteur (séparées par une virgule) : ").split(','))
    result(x1 * y2 - x2 * y1 == 0)


def result(r):
    clear(6)
    print("        _______________ ")
    print("       |               |")
    print("       |   AFFICHAGE   |")
    print("       |   RESULTATS   |")
    print("       |_______________|")
    clear(3)
    print("Le resultat est : ", r)
    sleep(1)
    home(1)


home(1)
