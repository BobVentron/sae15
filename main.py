import sujet2, sujet9, sujet15, sujet17
if __name__ == '__main__' :
    fini = False
    menu = """
        Tapez '1' pour le sujet 2
        Tapez '2' pour le sujet 9
        Tapez '3' pour le sujet 15
        Tapez '4' pour le sujet 17
        Taoez 'q' pour quitter.
        Votre choix : 
    """
    while (choix := input(menu)) not in 'qQ' :
        match choix : 
            case '1':
                sujet2.mainsujet2()
            case '2':
                sujet9.mainsujet9()
            case '3':
                sujet15.mainsujet15()
            case '4':
                sujet17.mainsujet17()
            case _: 
                print("Choix non valide")
