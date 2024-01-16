import anghour.sujet15
from gestion.gestionWeb import modifierWeb
from anghour.diagrammeAnghour import sujet15Graph
def mainAnghour(src : str, cheminData : str):
    """
    This function edits the website page 'anghour.html' using the results of various other methods such as 'modifyWeb', 'sujet18Graph', and 'mainsujet18'. 
    It takes two strings as parameters; one represents the path to access the CSV file containing the necessary information for the 'sujet15Graph' and 'mainsujet15' methods, and the second is the path to the 'data' file containing a configuration file.
    The method does not return anything; it simply edits the content of the website page.  
    """
    try :
        print("Livrable 1 sujet 15")
        tuple_diagramme = anghour.sujet15.mainsujet15(src, cheminData)
        modifierWeb("./www/anghour.html", "<!--Repere_Titre1-->", "<h4>Etude de l’étiage des cours d’eau  pour toutes les communes de naissance des étudiants du groupe.</h4>")
        sujet15Graph(src, tuple_diagramme)
        modifierWeb("./www/anghour.html", "<!--Repere_Titre2-->", "<h4>Diagrammes statistiques du nombre de cours d’eaux à sec en fonction des mois de l’année. </h4>")
        modifierWeb("./www/anghour.html","<!--Repere2-->", '<img src="medias/GraphAnghour.png" alt="histogramme">')
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type 1") #Display an error message.
    except e: #Any other error
        print(e) #Display an error message.