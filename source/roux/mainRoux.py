from roux.diagrammeRoux import histo9
from gestion.gestionWeb import modifierWeb as web
from roux.sujet9 import mainsujet9

def mainRoux(src, cheminData) -> None:
    try:
        """
        This function edits the website page 'roux.html' using the results of various other methods such as 'modifyWeb', 'histo9', and 'mainsujet9'. 
        It takes two strings as parameters; one represents the path to access the CSV file containing the necessary information for the 'histo9' and 'mainsujet9' methods, and the second is the path to the 'data' file containing a configuration file.
        The method does not return anything; it simply edits the content of the website page.  
        """
        print("Livrable 1 sujet 9")
        conso = mainsujet9(src, cheminData)                                                                                 #1st deliverable (electricity)
        histo9(src, cheminData)                                                                                             #create histogram
        web("./www/roux.html", "<!--Repere_Titre1-->", "<h4>Etude de la consommation résidentielle d'électricité</h4>")     #title
        for k in conso:                                                                                                     #browse dict
            web("./www/roux.html", "<!--Repere1-->", f"        <p>La commune de {k} a consommé {conso[k]:.2f}MWh en 2019</p>")  #electricity
        web("./www/roux.html", "<!--Repere_Titre2-->", "<h4>Diagramme de présentation pour chaque commune de naissance des étudiants du groupe de la consommation industrielle de gaz entre 2015 et 2020.</h4>")    #gaz
        web("./www/roux.html", "<!--Repere2-->", '        <img src="medias/GraphRoux.png" alt="histogramme">')              #print histogram
    except Exception as e:                                                                                                  #identify error
        print(f"Erreur mainRoux : {e}")                                                                                     #print it comes from here