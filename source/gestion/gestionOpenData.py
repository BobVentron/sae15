from gestion.gestionZip import extractionZip # import of files necessary for the operation

# import of necessary modules
from os import listdir, remove
from zipfile import BadZipFile

def supprimerFichierOpenData() -> None : 
    """
    This method deletes the useless files of the cache. This allows a clean cache.
    It doesn't take any parameter and doesn't return anything.
    """
    try : 
        for e in listdir("./opendata"):    
            if (".csv" in e) or (".pdf" in e): #Searchs all the useless file types and delete them.
                remove(f"./opendata/{e}")
    except FileNotFoundError as e : #Error if there is no usless files in the cache.
        print("erreur gestionOpenData, supprimerFichierOpenData: Il n'y a pas de fichiers inutiles a supprimer dans le cache")#Display an error message.
        print(e)
    except PermissionError as e : #Error if the user hasn't the permission to delete files.
        print("erreur gestionOpenData, supprimerFichierOpenData: Les fichiers n'ont pas pu être suprimés car vous n'en avez pas la permission")#Display an error message.
        print(e)#Displays an error message.
    except e: #Any other error.
        print(f"erreur gestionOpenData, supprimerFichierOpenData: {e}")#Displays an error message.

def extractsujet(src: str) -> str :
        """
        This function extracts a zip file, it takes 1 parameter which is the path of the zip file and returns the path of the extracted file
        """
        try :
            extractionZip(src, False)#Extracts all the files from the path provided by the user.
            if "opendata" in src:
                newsrc = (src[:-4] + ".csv")#Adds the type .csv to the file extracted from the path provided by the user. If the path passes trought the "opendata" file wich contains the data ZIP files, "opendata" file passage is removed.
            else :
                newsrc = (src[:-4] + ".csv").replace("./", "")#Adds the type .csv to the file extracted from the path provided by the user. If the path doen't pass trought the "opendata" file wich contains the data ZIP files, the "./" is removed to abreviate the path.
        except FileNotFoundError as e : #Error if the path doesn't exist.
            print(f"Erreur gestionOpenData, extractsujet: \n'{src}' n'existe pas!")#Displays an error message.
            print(e)
            exit()
        except PermissionError as e :#Error if the user hasn't the permission to extract the files.
            print(f"Erreur gestionOpenData, extractsujet: \nVous n'avez pas les droits sur '{src}'")#Displays an error message.
            print(e)
            exit()
        except BadZipFile as e : #Error if there is no file to extract in the path.
            print(f"Erreur gestionOpenData, extractsujet: \n{src} n'est pas un fichier zip")#Displays an error message.
            print(e)
            exit()
        else : 
            return newsrc # we don't forget to return the result of the function