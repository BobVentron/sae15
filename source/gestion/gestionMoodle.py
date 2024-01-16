# import of necessary modules
import statistics    
from csv import reader
import matplotlib.pyplot as plt

from gestion.gestionConfig import recupDonneeEtudiant # import of files necessary for the operation

def evalMoodle(cheminData: str):
    """
    This method provides the grade for each member of the group in the Moodle Evaluation. Additionally, it calculates the average grade, standard deviation, and the average time for the group. 
    It takes a string as a parameter, representing the path to the 'data' file containing the CSV file and configuration file. 
    The method returns a tuple consisting of: a dictionary containing the grades, a string representing the average grade, a string for the standard deviation, and a string for the average time
    """
    try:
        with open(f"{cheminData}/eval2_2023.csv", encoding='utf-8') as notes:#opening of the CSV file.
            lignesCSV=reader(notes, delimiter=';')
            nom_etudiants=recupDonneeEtudiant(f"{cheminData}/configuration.txt", "nom")
            dicoNote={}; temps=[]
            for lines in lignesCSV:        
                liste_note1=[]; liste_note2=[]; durée1=[]; durée2=[]
                if lines[0] in nom_etudiants:
                    #creation of the dictionary containing the grades
                    liste_note1=lines[3:]
                    for e in liste_note1:
                        liste_note2.append(float(e.replace(",",".")))
                    note=sum(liste_note2)
                    dicoNote[lines[0]]=note
                    #calculation of the average time
                    durée1=lines[2].split("min")#We collect the durations in the form of a list (the list separator is 'min', minutes are placed on one side and seconds on the other).
                    for e in durée1:
                        durée2.append(float(e.replace("s","")))#Creating a new list containing the numbers in float format, while removing unwanted letters (such as 's').
                    duréeSec=durée2[0]*60+durée2[1]#Creation of a variable containing the duration in seconds.
                    temps.append(duréeSec)#Storing durations in seconds in a list.
            temps_moy=sum(temps)/5#Calculation of the average time in seconds.
            temps_Moy=f"{temps_moy//60:.0f} min {temps_moy%60:.0f} s"#Decomposition of the average time into minutes and seconds, with the correct display.
            moyenne=sum(dicoNote.values())/5#calculation of the average grade
            ecart_type=statistics.stdev(dicoNote.values())#calculation of the standard deviation
            return dicoNote, f"{moyenne:.2f}", f"{ecart_type:.2f}", temps_Moy
    except FileNotFoundError as e: print(f"{cheminData} doesn't exist")#Error in case of an invalid path.
    except TypeError as e: print(f"{cheminData} has the wrong type")#Error in case of an invalid file type.
    except e:print(e) #Any other error 

def GraphMoodle(cheminData: str)->None:
    """
    This method creates a diagram containing the percentage of success for the group, corresponding to each question of the Moodle evaluation. 
    It takes a string as a parameter, which represents the path to the 'data' file containing the CSV file and configuration file. 
    The method does not return anything; it simply saves the diagram.
    """
    dicomax={}; diconote={}; dicoresult={}
    try:
        with open(f"{cheminData}/eval2_2023.csv", encoding='utf-8') as notes:#opening of the CSV file.
            lignesCSV=reader(notes, delimiter=';')
            nom_etudiants=recupDonneeEtudiant(f"{cheminData}/configuration.txt", "nom")
            for lines in lignesCSV:#Creation of the dictionary contaning the maximal grade for each question of the moodle evaluation.
                for e in range(3,len(lines)):
                    notemax=float(lines[e].replace(",","."))
                    if notemax > dicomax.get(e,0):
                        dicomax[e]=notemax
            notes.seek(0)
            lignesCSV2=reader(notes, delimiter=';')
            for lines in lignesCSV2:#Creation of the dictionary containing the number of people in the group who have the highest grade.
                if lines[0] in nom_etudiants:
                    for x in range(3,len(lines)):
                        note=float(lines[x].replace(",","."))
                        if note == dicomax[x]:
                            diconote[x-2]=diconote.get(x-2,0)+1
                        else:
                            diconote[x-2]=diconote.get(x-2,0)
            diconote=dict(sorted(diconote.items()))
            for k in diconote:#Creation of the dictionary containing the percentage of success of the group for each question.
                diconote[k]=diconote.get(k)/5*100; a=f"{k}"
                dicoresult[a]=diconote.get(k)
        plt.subplots(figsize=(15,6))#Creation of the diagramm
        plt.bar(dicoresult.keys(), dicoresult.values(), color='blue')
        plt.xlabel('Numéro de la question'); plt.ylabel('Pourcentage de réussite'); plt.title(f"Pourcentage de réussite des questions pour le groupe")
        plt.savefig("./www/medias/GraphMoodle")
    except FileNotFoundError as e: print(f"{cheminData} doesn't exist")#Error in case of an invalid path.
    except TypeError as e: print(f"{cheminData} has the wrong type")#Error in case of an invalid file type.
    except e:print(e) #Any other error 

                    


            
