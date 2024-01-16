def mainsujet18(src : str, cheminData: str) -> dict :  
    """
    This method gives, for each places of birth of the members of the group, the number of rent observations in 2022.
    It takes a string as parameter wich is the path to the CSV file containing the data to extract.
    The method doesn't returns anything, it just displays the number of rent observations.
    """
    from csv import reader
    from gestion.gestionConfig import recupDonneeEtudiant
    nom_communes=recupDonneeEtudiant(f"{cheminData}/configuration.txt", "communes")
    code_communes=recupDonneeEtudiant(f"{cheminData}/configuration.txt", "codeINSEE")
    dico1={}
    try: #normal code running.
        with open(src, encoding='utf-8') as observations:#opening of the CSV file.
            lignesCSV=reader(observations, delimiter=';')
            next(lignesCSV)#Skip one line.
            for lines in lignesCSV:
                if (lines[2] in nom_communes) and (lines[1] in code_communes): # Searchs for each lines of the file, the name and the INSEE code of the places of birth of the group members.
                    dico1[lines[2]]=lines[10]
                    print(f"Il y a eu {lines[10]} observations de loyers dans la commune de {lines[2]} en 2022")#Displays the results.
        return dico1
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist")#Displays an error message.
    except PermissionError as e :#Error in case of denied permission.
        print(f"You don't have the permissions on {src}")#Displays an error message.
    except TypeError as e:#Error in case of an invalid file type.
        print(f"{src} has the wrong type")#Displays an error message.
    except e:#Any other error.
        print(e)#Displays an error message.
    