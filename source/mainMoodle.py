
from gestion.gestionWeb import modifierWeb as web
from gestion.gestionMoodle import evalMoodle
from gestion.gestionMoodle import GraphMoodle

def pageMoodle(cheminData):
    """
    This function edits the website page 'index.html' using the results of various other methods such as 'modifierWeb', 'evalMoodle', and 'GraphMoodle'. 
    It takes on strings as parameter which is the path to the 'data' file containing a configuration file and a csv file on the Moodle evaluation.
    The method does not return anything; it simply edits the content of the website page.  
    """
    GraphMoodle(cheminData)
    stats=evalMoodle(cheminData)
    web("./www/index.html", "<!--Repere_Titre1-->","<h4>Notes des etudiants du groupe</h4>" )
    dico_notes=stats[0]
    for k in dico_notes:
        web("./www/index.html", "<!--Repere1-->", f"<p>{k} : {dico_notes[k]:.2f}</p>" )
    web("./www/index.html", "<!--Repere_Titre2-->","<h4>Statistiques sur le groupe</h4>" )
    web("./www/index.html", "<!--Repere2-->",f"<p>Moyenne : {stats[1]}</p>" )
    web("./www/index.html", "<!--Repere2-->",f"<p>Ecart type : {stats[2]}</p>" )
    web("./www/index.html", "<!--Repere2-->",f"<p>Temp moyen : {stats[3]}</p>" )
    web("./www/index.html", "<!--Repere_Titre3-->","<h4>Pourcentage de reussite de chaque question pour le groupe</h4>" )
    web("./www/index.html", "<!--Repere3-->", '        <img src="medias/GraphMoodle.png" alt="histogramme">')