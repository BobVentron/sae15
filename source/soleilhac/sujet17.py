import csv #Importing the CSV module

def mainsujet17(src : str, CommunesNaissance: list, classe: str) -> dict : 
    '''
        This function returns the number of students of a level
        The first parameter (src) which is a string : holds the access path to a csv file.
        The second parameter is the list of municipalities of the students in the group
        the last parameter is the class which must be one of this list: cp, ce1, ce2, cm1, cm2
        This fonction doesn't return anything.
    '''
    try : 
        with open(src, encoding='utf-8') as file : #opening the csv file 
            lignesEcole= csv.reader(file, delimiter=';') #transformation of the csv file into a list that can be understood by the program
            next(lignesEcole) #we skip the first line because it contains the methadata from the csv  
            result = {communes: 0 for communes in CommunesNaissance} #dictionary which is built from the list above and which will contain the results
            for ligne in lignesEcole : #we go through all the lines in our csv
                commune = ligne[4]
                if commune in CommunesNaissance:            #If we find a commune that is on our list,
                    match classe :
                        # we add the number of pupils to the correct commune. 
                        case 'cp' : result[commune] += int(ligne[16])       
                        case 'ce1': result[commune] += int(ligne[17])   
                        case 'ce2': result[commune] += int(ligne[18]) 
                        case 'cm1': result[commune] += int(ligne[19]) 
                        case 'cm2': result[commune] += int(ligne[20]) 
        return result # we don't forget to return the result of the function
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"Erreur sujet17 : {src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"Erreur sujet17 : You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"Erreur sujet17 : {src} has the wrong type") #Display an error message.
    except Exception as e: #Any other error
        print(f"Erreur sujet17 : {e}") #Display an error message.
