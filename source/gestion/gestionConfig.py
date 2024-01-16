import csv # import of necessary modules

def recupDonneeEtudiant(srcConfig : str, whatData : str) -> list :
    """
    function which allows you to extract data from the 'configuration.txt' file. This function takes 2 parameters
        -the first parameter is the path to the configuration file
        -the second parameter is what need to be retrieved in the latter
        -this function returns a list of data
    """
    try :
        liste = []
        with open(srcConfig, "r", encoding="utf-8") as config: # opening the csv file 
            lignesConfig= csv.reader(config, delimiter=':') # transformation of the csv file into a list that can be understood by the program
            for ligne in lignesConfig : # we go through all the lines in our csv
                if "etudiant " in ligne : # we look if the line corresponds to a line having the data of a student

                    #we select the desired data, have the extract and put it in a list
                    match whatData: 
                        case "nom": liste.append(ligne[1].replace(" ", ""))
                        case "login": liste.append(ligne[3].replace(" ", ""))
                        case "codePostaux": liste.append(int(ligne[5].replace(" ", "")))
                        case "communes": liste.append(ligne[6].replace(" ", ""))
                        case "sujet": liste.append(ligne[8].replace(" ", ""))
                        case "codeINSEE": liste.append(ligne[7].replace(" ", ""))
                        case "prenon": liste.append(ligne[2].replace(" ", ""))

    # handling of the various errors that may occur during the execution of the function
    except FileNotFoundError:
        print(f"Erreur gestionconfig, recupDonneeEtudiant: Le fichier {srcConfig} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur gestonconfig, recupDonneeEtudiant : Une erreur s'est produite dans recupDonneeEtudiant : {e}")
    else :
        return liste # we don't forget to return the result of the function

def recupCheminData(srcConfig : str) -> list :
    """
    This function allows you to retrieve the path of the subject csvs of each student. 
    It takes a single parameter which is the path to the configuration file.
    this function returns a list of data
    """
    try :
        listeSujet = recupDonneeEtudiant(srcConfig, "sujet") # retrieval of the list of subjects of the students of the group
        newListeSujet = []

        # we find the right name for the rest of the function
        for sujet in listeSujet:
            newListeSujet.append((f"sujet_{sujet[5:]}").replace(" ", "")+" ")

        liste = []
        with open(srcConfig, "r", encoding="utf-8") as config: # opening the csv file 
            lignesConfig= csv.reader(config, delimiter=':') # transformation of the csv file into a list that can be understood by the program
            for ligne in lignesConfig : # we go through all the lines in our csv
                for elem in newListeSujet : 
                    if elem in ligne : # we look to see if we find the right name in the csv file
                        liste.append(ligne[1].replace(" ","")) # we retrieve the name of the csv that interests us

    #handling of the various errors that may occur during the execution of the function                    
    except FileNotFoundError:
        print(f"Erreur gestionconfig, recupCheminData: Le fichier {srcConfig} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur gestionconfig, recupCheminData: {e}")
    else :
        return liste # we don't forget to return the result of the function