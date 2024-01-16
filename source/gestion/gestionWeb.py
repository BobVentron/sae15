# import of necessary modules
from datetime import datetime
from shutil import make_archive, rmtree, copy
from os import listdir, remove

def modifierWeb(src: str, where: str, what: str) -> None:
    '''
    This function allows you to add a line to a file. Here we will use it to add elements to a web page. It has three parameters and it returns nothing 
    The first parameter is the path of the file to modify
    The second parameter is the indicator where you want to add the line
    And the last parameter is what you want to add
    '''
    try :
        #opening the file to modify in read only
        with open(src, "r", encoding="utf-8") as htmlfile:
            lines = htmlfile.readlines()

        with open(src, "w",  encoding="utf-8") as htmlfile: # opening the file to modify for writing
            for line in lines: #we go through all the lines of the file
                htmlfile.write(line)
                if where in line: # we test if we find our indicators in the line
                    htmlfile.write(what + "\n") # if we find it we add what is necessary

    #handling of the various errors that may occur during the execution of the function 
    except FileNotFoundError as e: print(f"Erreur gestionWeb, modifierWeb : le fichier a modifier n'a pas été trouver, \n {e}")
    except PermissionError as e: print(f"Erreur gestionWeb, modifierWeb : problème de permission sur le fichier a modifier \n {e}")
    except IsADirectoryError as e: print(f"Erreur gestionWeb, modifierWeb : le fichier à modifier n'est pas un fichier mais un repertoire \n {e}")
    except e : print(f"Erreur gestionWeb, modifierWeb : {e}")

def sauvegardeWeb(srcWeb: str="./www", scrSauvegarde: str="./sauvegarde") -> None:
    """
    This function allows you to make a backup of a website. It takes parameters, the first is the path of the website to save and the second is the path of the folder where to save it. It returns nothing.
    """
    try :
        date = datetime.now().strftime("%Y-%m-%d.%Hh%Mm%Ss") # get today's time and date
        make_archive(f"{scrSauvegarde}/sauvegarde_web_{date}", 'zip', srcWeb) # creates a zip archive with the right name and in the right place

    #handling of the various errors that may occur during the execution of the function 
    except NotADirectoryError as e : print(f"Erreur gestionWeb, sauvegarderWeb : le dossier n'est pas un dossier, \n {e}")
    except FileNotFoundError as e: print(f"Erreur gestionWeb, sauvegarderWeb : le fichier a modifier n'a pas été trouver, \n {e}")
    except PermissionError as e : print(f"Erreur gestionWeb, sauvegarderWeb : problème de permission sur le fichier a sauvegarder \n {e}")
    except OSError as e: print(f"Erreur gestionWeb, sauvegarderWeb : OSError, \n{e}")
    except e : print(f"Erreur gestionWeb, sauvegardeWeb : {e}")

def supprimerWeb(srcwww: str="./www", parms: bool=True) -> None : 
    """
    This function allows you to delete a file or folder. It takes two parameters but returns nothing.
    The first parameter is the path of the file or folder to delete.
    The second parameter one is boolean, when it is True it means that it is a file to be deleted and when it is false it means that it is a file to be deleted.
    """
    try : 
        if parms :
            rmtree(srcwww) # delete a folder
        else :
            remove(srcwww) # delete a file
    except FileNotFoundError as e : #Error if there is no usless files in the cache.
        print("Erreur gestionWeb, supprimerWeb : Il n'y a pas de fichiers inutiles a supprimer dans le cache")#Display an error message.
        print(e)
    except PermissionError as e : #Error if the user hasn't the permission to delete files.
        print("Erreur gestionWeb, supprimerWeb : Les fichiers n'ont pas pu être suprimés car vous n'en avez pas la permission")#Display an error message.
        print(e)#Displays an error message.
    except OSError as e:
        print(f"Erreur gestionWeb, supprimerWeb : Erreur lors de la suppression du fichier {srcwww}: {e}")
    except e: #Any other error.
        print("Erreur gestionWeb, supprimerWeb :")
        print(e)#Displays an error message.

def clonnerPageWeb(src: str, nouveau_nom : str, nom, prenon) -> None:
    """
    This function allows you to clone web pages by modifying them. It takes 4 parameters and returns nothing.
    the first parameter is the path of the file to copy
    the second is the name that the new file should have
    the third and fourth parameters are respectively the name and first name of the person who owns the web page
    """
    try:
        copy(src, nouveau_nom) # copy the page and rename it
        
    #handling of the various errors that may occur during the execution of the function 
    except FileNotFoundError as e:
        print(f"Erreur gestionWeb, clonnerPageWeb : Le fichier source n'a pas été trouvé, \n {e}")
    except PermissionError as e:
        print(f"Erreur gestionWeb, clonnerPageWeb: Permission refusée lors de la copie du fichier, \n {e}")
    except Exception as e:
        print(f"Erreur gestionWeb, clonnerPageWeb: lors de la copie du fichier : {e}")
    else:
        #modify the page with the correct first and last name
        modifierWeb(nouveau_nom, "<!--Repere_author-->", f'<meta name="author" content="{prenon} {nom}">')
        modifierWeb(nouveau_nom, "<!--Repere_Titre_Page-->", f'<h1> Page de {prenon} {nom} </h1>')
        modifierWeb(nouveau_nom, "<!--Repere_Footer-->", f'<p>{nom} {prenon}</p>')
        try:
            listfichier = listdir("./www") # retrieve the list of files present in './www'

        #handling of the various errors that may occur during the execution of the function 
        except FileNotFoundError as e:
            print(f"Erreur gestionWeb, clonnerPageWeb: : Le répertoire spécifié n'a pas été trouvé \n {e}")
        except PermissionError as e:
            print(f"Erreur gestionWeb, clonnerPageWeb: : Permission refusée pour accéder au répertoire \n {e}")
        except Exception as e:
            print(f"Erreur gestionWeb, clonnerPageWeb: lors de la liste des fichiers : {e}")
        else :
            # adds access to the new web page to the website navigation bar
            for fichier in listfichier:
                if ".html" in fichier:
                    modifierWeb(f"./www/{fichier}", "<!--Repere_navbar-->",f'<a class="hover_nav_element" href="{nom.lower()}.html">Page {nom}</a>')