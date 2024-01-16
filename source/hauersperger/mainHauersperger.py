from gestion.gestionWeb import modifierWeb as web
import hauersperger.sujet18
from hauersperger.diagrammeHauersperger import sujet18Graph

def mainHauersperger(src, cheminData):
    """
    This function edits the website page 'hauersperger.html' using the results of various other methods such as 'modifyWeb', 'sujet18Graph', and 'mainsujet18'. 
    It takes two strings as parameters; one represents the path to access the CSV file containing the necessary information for the 'sujet18Graph' and 'mainsujet18' methods, and the second is the path to the 'data' file containing a configuration file.
    The method does not return anything; it simply edits the content of the website page.  
    """
    try:
        print("Livrable 1 sujet 18")
        observations=hauersperger.sujet18.mainsujet18(src, cheminData)
        sujet18Graph(src, cheminData)
        web("./www/hauersperger.html", "<!--Repere_Titre1-->", "<h4>Etude du nombre d'observations de loyers pour chaque commune de naissance des étudiants du groupe</h4>")
        for k in observations:
            web("./www/hauersperger.html", "<!--Repere1-->", f"        <p>Il y a eu {observations[k]} observations de loyer en 2022 dans la commune de {k}</p>")
        web("./www/hauersperger.html", "<!--Repere_Titre2-->", "<h4>Histogrammes donnant, pour chaque département de naissance des étudiants du groupe, le nombre de communes en fonctions de l'indicateurs de loyer en €/m2 (par pas de 0.5€).</h4>")
        web("./www/hauersperger.html", "<!--Repere2-->", '        <img src="medias/GraphDrome.png" alt="histogramme">')
        web("./www/hauersperger.html", "<!--Repere2-->", '        <img src="medias/GraphIsere.png" alt="histogramme">')
        web("./www/hauersperger.html", "<!--Repere2-->", '        <img src="medias/GraphLoire.png" alt="histogramme">')
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type") #Display an error message.
    except e: #Any other error
        print(e) #Display an error message.


    