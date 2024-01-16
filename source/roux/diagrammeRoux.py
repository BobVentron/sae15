from csv import reader
from gestion.gestionConfig import recupDonneeEtudiant
import matplotlib.pyplot as plt

def get(src : str, cheminData : str) -> dict: 
    """
    Get the datas of gas consumption for each of the group's students' home towns (list)
    industrial gas consumption between 2015 and 2020.
    """
    communes={}
    try:
        for e in recupDonneeEtudiant(f"{cheminData}/configuration.txt", "communes"):                #get the datas
            communes[e]=0                                                                           #fill values with 0
        with open(src, "r", encoding="utf-8") as raw:                                               #open and store the file
            database = reader(raw, delimiter=';')                                                   #split into different categories
            next(database)                                                                          #next item from the iterator
            for line in database:                                                                   #line: list
                if int(line[1]) <= 2020 and int(line[1]) >= 2015 and line[26] in communes and int(line[33]) == 200:
                #26 corresponds to the category commune name and 33 to verify if it's electricity (100) or gaz (200)
                    communes[line[26]] += float(line[7])                                            #consoi corresponds to line 7
        return communes                                                                             #communes: dict
    except FileNotFoundError as e:                          #Error in case of an invalid path.
        print(f"{src} doesn't exist")                       #Display an error message.
    except PermissionError as e :                           #Error in case of denied permission.
        print(f"You don't have the permissions on {src}")   #Display an error message.
    except TypeError as e:                                  #Error in case of an invalid file type.
        print(f"{src} has the wrong type")                  #Display an error message.
    except e:                                               #Any other error
        print(e)                                            #Display an error message.



def histo9(src : str, cheminData : str) -> None:
    """
    Create the histogram based on datas from get method
    Return None as it saves the graph in medias
    """
    gaz=""
    x = get(src, cheminData).keys()                                                                         #x-axis
    y = get(src, cheminData).values()     
    plt.subplots(figsize=(15,6))                                                                  #y-axis
    plt.bar(x, y, color = "#4CAF50")                                                                        #creation
    font1 = {'family':'serif','color':'black','size':12}                                                    #font for title
    font2 = {'family':'serif','color':'gray','size':10}                                                     #font for subtitles
    plt.xlabel('Communes', fontdict=font2)                                                                  #x-axis name
    plt.ylabel('Consommation industrielle de gaz', fontdict=font2)                                          #y-axis name
    plt.title("Consommation industrielle des communes entre 2015 et 2020", fontdict=font1, loc="left")   #title settings
    plt.grid(axis='y', linewidth=0.5)                                                                       #grid settings                     
    plt.savefig(f"./www/medias/GraphRoux{gaz}")                                                             #save