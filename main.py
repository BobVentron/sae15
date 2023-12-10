import sujet2, sujet9, sujet15, sujet18, sujet17
from zipfile import ZipFile, BadZipFile
from os import remove, listdir

def quitter() -> None : 
    quitter = input("êtes vous sur de vouloir quitter ? \n Tapez 'oui' ou 'non' :")
    if quitter in ["oui", "OUI", "o", "O"]:
        print("Good bye!")
        exit()

def extractionZip(src : str) -> None : 
    with ZipFile(src, 'r') as zip:
        zip.extractall('opendata')   

def supprimerFichier(src : str) -> None : 
    try : 
        for e in listdir("opendata"): 
            if ".zip" not in e:
                remove("./opendata/"+ e)
    except FileNotFoundError as e : 
        print("test1")
    except PermissionError as e :
        print("Le fichiers n'a pas pue être suprimé car pas le perm")
    except TypeError as e :
        print("le chemins d'acces au fichier doit être une chaine de caractère!")

def paramtre(sujet : int) -> str :
    fini2 = False
    
    while not fini2: 
        match sujet :
            case 2: src = "./opendata/trace.zip"
            case 9: src = "./opendata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-commune.zip"
            case 15: src = "./opendata/onde_france_2022.zip"
            case 17 : src = "./opendata/fr-en-ecoles-effectifs-nb_classes.zip"
            case 18: src = "./opendata/pred-app3-mef-dhup.zip"

        menu = f"Tapez 'oui' si vous vouler modifier le chemin d'acces au donnés ou 'non' dans le cas contraire. \n Si vous changer pas le chemin celui utiliser sera : {src} \n Votre choix : "
        
        try : var = input(menu)
        except KeyboardInterrupt: quitter()
        else : 
            if var in ["OUI", "oui", "o", "O"]: 
                src = input("Entrez votre chemins d'accès : ")
        try :
            extractionZip(src)
            if "opendata" in src:
                newsrc = src[:-4] + ".csv"
            else :
                newsrc = ("./opendata/" + src[:-4] + ".csv").replace("./", "")
            fini2 = True
        except FileNotFoundError as e :
            print(f"'{src}' n'existe pas!")
        except PermissionError as e :
            print(f"Vous n'avez pas les droits sur '{src}'")
        except BadZipFile as e :
            print(f"{src} n'est pas un fichier zip")
            
    return newsrc       

if __name__ == '__main__' :
    fini1 = False
    menu = """
        Tapez '1' pour le sujet 2
        Tapez '2' pour le sujet 9
        Tapez '3' pour le sujet 15
        Tapez '4' pour le sujet 17
        Tapez '5' pour le sujet 18
        Tapez 'q' pour quitter.
        Votre choix : 
    """
    
    while not fini1:
        try : choix = input(menu)
        except KeyboardInterrupt : quitter()
        else :
            match choix : 
                case '1':
                    src = paramtre(2)
                    sujet2.mainsujet2(src)
                    supprimerFichier(src)
                case '2':
                    src = paramtre(9)
                    sujet9.mainsujet9(src)
                    supprimerFichier(src)
                case '3':
                    src = paramtre(15)
                    sujet15.mainsujet15(src)
                    supprimerFichier(src)
                case '4':
                    src = paramtre(17)
                    sujet17.mainsujet17(src)
                    supprimerFichier(src)
                case '5':
                    src = paramtre(18)
                    sujet18.mainsujet18(src)
                    supprimerFichier(src)
                case 'q': quitter()
                case 'Q': quitter()
                case _: print("Choix non valide")