from csv import reader
from gestion.gestionConfig import recupDonneeEtudiant

def mainsujet9(src: str, cheminData: str) -> dict : 
    """
    Give the total residential electricity consumption "consor" (MWh)
    for all the communes in which the group's students were born.
    Those communes are given in argument as src and return None
    """
    communes={}
    try:
        for e in recupDonneeEtudiant(f"{cheminData}/configuration.txt", "communes"):        #get the datas
            communes[e]=0                                                                   #fill values with 0
        with open(src, "r", encoding="utf-8") as raw:                                       #open and store the file
            database = reader(raw, delimiter=';')                                           #split into different categories
            next(database)                                                                  #next item from the iterator
            for line in database:                                                           #line: list
                if int(line[1]) == 2019 and line[26] in communes and int(line[33]) == 100:
                    #1 corresponds to date ; 26 corresponds to commune name ; 33 corresponds to electricity when '100'
                    communes[line[26]] += float(line[15])                                   #consor corresponds to line 15
        print("Communes correspondant à la consommation résidentielle :")      #return dico
        for communeconso in communes : print(f"{communeconso} a comme consommation résidentielle  de : {communes[communeconso]:.2f} MWh.")
        return communes                                                                     #communes: dict
    except FileNotFoundError as e:                          #Error in case of an invalid path.
        print(f"{src} doesn't exist")                       #Display an error message.
    except PermissionError as e :                           #Error in case of denied permission.
        print(f"You don't have the permissions on {src}")   #Display an error message.
    except TypeError as e:                                  #Error in case of an invalid file type.
        print(f"{src} has the wrong type")                  #Display an error message.
    except e:                                               #Any other error
        print(e)                                            #Display an error message.