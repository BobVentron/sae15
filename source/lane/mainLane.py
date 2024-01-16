#__________________________________________________________________________________________________
from lane.sujet2 import mainsujet2  
from lane.diagrammeLane import sujet2Graph            # Importations of the libraries
from gestion.gestionWeb import modifierWeb as web
from gestion.gestionConfig import recupDonneeEtudiant
#__________________________________________________________________________________________________

def mainLane(src : str, CheminData : str):
    """
    This function edits the website page 'hauersperger.html' using the results of various other functions such as 'mainsujet2', 'sujet2Graph', and 'modifierWeb' . 
    It takes two strings as parameters; one represents the path to access the CSV file containing the necessary information for the 'sujet18Graph' and 'mainsujet18' functions, and the second is the path to the 'data' file containing a configuration file.
    It doesn't return anything; it simply edits the content of the website page.  
    """
    print("Livrable 1 sujet 2")
    listelogin = recupDonneeEtudiant(f"{CheminData}/configuration.txt", "login")
    # This line collects the observations using the mainsujet2 function
    observations = mainsujet2(src, listelogin, "b")

    # This line calls the sujet2Graph function
    sujet2Graph(src, CheminData)

    # This line adds the 1st title to the lane.html file
    web("./www/lane.html", "<!--Repere_Titre1-->", "<h4>Etude du nombre de « hits » pour chaque élève du groupe grâce à leur login </h4>")
    
    # Thoses lines add the observations to the lane.html file
    for key, value in observations.items():
        web("./www/lane.html", "<!--Repere1-->", f"<p>{key} a {value} hits.</p>")
        print(f"{key} a {value} hits.")
    
    # Thoses lines add the 2nd title and the histogram to the lane.html file
    web("./www/lane.html", "<!--Repere_Titre2-->", "<h4>Histogramme pour les membres du groupe par bloc de 4h du nombre total de « hits »</h4>")
    web("./www/lane.html", "<!--Repere2-->", '<img src="medias/GraphLane.png" alt="histogramme">')