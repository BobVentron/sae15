from soleilhac.sujet17 import mainsujet17
from gestion.gestionWeb import modifierWeb
from gestion.gestionConfig import recupDonneeEtudiant
from soleilhac.diagrammeSoleilhac import diagramme

from unicodedata import normalize, category


def mainSoleilhac(src, cheminData):
    try : 
        print("Livrable 1 sujet 17")
        listecommune = recupDonneeEtudiant(f"{cheminData}/configuration.txt", "communes")
        newCommune = []
        for commune in listecommune : newCommune.append(''.join(c for c in normalize('NFD', commune.upper()) if category(c) != 'Mn'))

        eleveEnCp =  mainsujet17(src, newCommune, "cp")
            
        modifierWeb("./www/soleilhac.html", "<!--Repere_Titre1-->", "<h4>Etude du nombre d'élèves en CP pour les communes de naissance de chaque étudiants du groupe.</h4>")
        for communes in newCommune : 
            modifierWeb("./www/soleilhac.html", "<!--Repere1-->", f'<p>Dans la commune de {communes.lower()} il y a : {eleveEnCp[communes]} enfant en classe de CP.</p>')
            print(f"Dans la commune de {communes.lower()} il y a : {eleveEnCp[communes]} enfant en classe de CP.")
        diagramme(src, newCommune, listecommune)
        modifierWeb("./www/soleilhac.html", "<!--Repere_Titre2-->", "<h4>Histogramme donnant, la répartition des élèves en classes de CP, CE1, CE2, CM1, CM2, pour chaque commune de naissance des étuduantes du groupe.</h4>")
        modifierWeb("./www/soleilhac.html", "<!--Repere2-->", f'<img src="medias/GraphSoleilhac.png" alt="histogramme">')
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type") #Display an error message.
    except Exception as e: #Any other error
        print(e) #Display an error message.