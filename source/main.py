# import of necessary modules
import sys          
import webbrowser   
import os           

# import of files necessary for the operation of the main
from gestion.gestionWeb import sauvegardeWeb, supprimerWeb, clonnerPageWeb  
from gestion.gestionZip import extractionZip, renommerFichier               
from gestion.gestionConfig import recupDonneeEtudiant, recupCheminData      
from gestion.gestionOpenData import extractsujet, supprimerFichierOpenData  
from mainMoodle import pageMoodle                                           

#importing files (of the main function) of each person
from anghour.mainAnghour import mainAnghour                 
from hauersperger.mainHauersperger import mainHauersperger  
from lane.mainLane import mainLane                          
from roux.mainRoux import mainRoux                          
from soleilhac.mainSoleilhac import mainSoleilhac           

fonctions = { # dictionary used to dynamically call the main functions of each person
    'Anghour': mainAnghour,
    'Hauersperger': mainHauersperger,
    'Lane': mainLane,
    'Roux': mainRoux,
    'Soleilhac': mainSoleilhac,
}

if __name__ == '__main__' :
    reponse1 = """ 
        Vous devez mettre 2 paramètres en appellant la fonction.
        Le premiers paramètre est le chemin vers le fichier de data. 
        Le deuxième est le chemin vers le dossier d'opendata
    """ # The response will return to the user if he calls the program with incorrect settings
    try :
        #recovery of parameters given during the program call
        cheminData=sys.argv[1]      
        cheminOpendata=sys.argv[2]  
    #error in the parameters entered when calling the program
    except IndexError as e: print(reponse1) 
    except Exception as e: print(e)         
    else :

        sauvegardeWeb() # calls the sauvegarderWeb function which allows you to save and zip the 'www' file
        supprimerWeb() # calls the extractionWeb function which deletes the 'www' file
        extractionZip() # calls the extractionWeb function which unzip the 'template_www.zip' file
        renommerFichier("./template_www", "./www") #calls the renommerFichier function which renames the 'template_www' file to 'www'

        #calls the function recupDonneeEtudiant which allows the recovery of the data of the students of the group that interests us
        listeNom = recupDonneeEtudiant(f"{cheminData}/configuration.txt", "nom") 
        listePrenom = recupDonneeEtudiant(f"{cheminData}/configuration.txt", "prenon") 
        listeSujet = recupDonneeEtudiant(f"{cheminData}/configuration.txt", "sujet")

        listeCheminSujet =  recupCheminData(f"{cheminData}/configuration.txt") # calls the function recupCheminData which allows the recovery of the paths or the location of the csv
        
        #Dynamic creation of web pages for each member of the group using the clonnerPageWeb function
        compt = 0
        for nom in listeNom:
            clonnerPageWeb("./www/templates_page_perso.html", f"./www/{nom.lower()}.html", nom, listePrenom[compt])
            compt += 1
        supprimerWeb("./www/templates_page_perso.html", False) #deletion of the file which we used as a template to generate the pages of each student in the group

        # dynamic execution of files for each student in the group       
        compt = 0 
        for nom in listeNom :
            try:
                src = extractsujet(f"{cheminOpendata}/{listeCheminSujet[compt]}")
                fonction_main = fonctions[nom]
                fonction_main(src, cheminData)
            except KeyError as e: print(f"Nom de fonction non trouvé dans le dictionnaire : {e}")
            except Exception as e: print(f"Erreur lors de l'exécution de la fonction pour {nom}: {e}")
            compt += 1
        
        # calls the function relating to the web page 'synthese'
        try:
            pageMoodle(cheminData)
        except KeyError as e: 
            print(f"Nom de fonction non trouvé dans le dictionnaire : {e}")
        except Exception as e: 
            print(f"Erreur lors de l'exécution de la fonction pageMoodle : {e}")
        supprimerFichierOpenData()
        
        # opening and displaying the website
        try:
            indexHTML = os.path.abspath("./www/index.html")
            webbrowser.open("file://" + indexHTML)
        except FileNotFoundError as e:
            print(f"Erreur : Le fichier index.html n'a pas été trouvé, \n {e}")
        except webbrowser.Error as e:
            print(f"Erreur lors de l'ouverture du navigateur web, \n {e}")
        except Exception as e:
            print(f"Erreur inattendue lors de l'ouverture de index.html, \n {e}")