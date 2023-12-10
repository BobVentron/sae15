def mainsujet18(src : str) -> None : 
    from csv import reader
    communes=["Roussillon","Voiron","Romans-sur-Is","Cellieu"]
    with open(src,"r") as observations:
        lignesCSV=reader(observations, delimiter=';')
        next(lignesCSV)
        for lines in lignesCSV:
            for e in communes:
                if e in lines[2] and "Roussillon" not in lines[2]:
                    print(f"Il y a eu {lines[10]} observations de loyers dans la commune de {lines[2]} en 2022")
            if "Roussillon" in lines[2] and "-" not in lines[2] and "38" in lines[1]:
                print(f"Il y a eu {lines[10]} observations de loyers dans la commune de {lines[2]} en 2022")    