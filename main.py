if __name__ == '__main__' :
    fini = False
    menu = """
        Tapez '1' pour ...
        Tapez '2' pour ...
        Taoez 'q' pour quitter.
        Votre choix : 
    """
    while (choix := input(menu)) not in 'qQ' :
        match choix : 
            case '1':
                print("Choix 1")
            case '2':
                print("Choix ")
            case _: 
                print("Choix non valide")
