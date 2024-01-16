# import of necessary modules
from zipfile import ZipFile, BadZipFile
from os import rename

def extractionZip(src : str="./source/template_www.zip", parms: bool=True) -> None : 
    """
    This method extracts the CSV files from ZIP files.
    It takes for parameter a string wich is the path to the ZIP files.
    The second parameter is a boolean, if it is true then the file will be extracted at the root of the project and if it is false it will be extracted in the 'opendata' file.
    It doen't return anything.
    """
    try :
        with ZipFile(src, 'r') as zip:
            if parms :
                zip.extractall() # extract the file from the root
            else :
                zip.extractall('opendata') # extract the file into the 'opendata' file
    
    #handling of the various errors that may occur during the execution of the function 
    except FileNotFoundError as e:
        print(f"Erreur gestionZip, extractionZip: Le fichier ZIP ({src}) spécifié n'a pas été trouvé \n {e}")
    except BadZipFile as e:
        print(f"Erreur gestionZip, extractionZip: Le fichier spécifié ({src}) n'est pas un fichier ZIP valide \n {e}")
    except PermissionError as e:
        print(f"Erreur gestionZip, extractionZip: Permission refusée pour accéder au fichier ZIP ({src}) \n {e}")
    except Exception as e:
        print(f"Erreur gestionZip, extractionZip :lors de l'extraction du fichier ZIP ({src}) : {e}")
            
def renommerFichier(ancien_nom, nouveau_nom) -> None:
    """
    This function allows you to rename a file, it does not change anything.
    the first parameter is the link of the file to be renamed
    and the second is the new name of the file.
    """
    try:
        rename(ancien_nom, nouveau_nom) # rename the file

    #handling of the various errors that may occur during the execution of the function 
    except FileNotFoundError as e:
        print(f"Erreur gestionZip, renommerFichier: Le fichier '{ancien_nom}' n'a pas été trouvé, \n {e}")
    except PermissionError as e:
        print(f"Erreur gestionZip, renommerFichier: Permission refusée pour renommer le fichier '{ancien_nom}', \n {e}")
    except Exception as e:
        print(f"Erreur gestionZip, renommerFichier: lors du renommage du fichier '{ancien_nom}' : {e}")