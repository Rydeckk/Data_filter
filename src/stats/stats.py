from utils.utils import is_boolean, is_numeric, is_list


def print_structure_stats(structure):
    stats = {}
    for ligne in structure:
        for champ in ligne:
            valeursNum = [s[champ] for s in structure if is_numeric(s[champ])]
            if valeursNum:
                stats[champ] = {
                    'type': 'numerique',
                    'min': min(valeursNum),
                    'max': max(valeursNum),
                    'moyenne': sum(valeursNum) / len(valeursNum)
                }
                continue

            valeursBool = [s[champ] for s in structure if is_boolean(s[champ])]
            if valeursBool:
                pourcentTrue = sum(valeursBool) / len(valeursBool) * 100
                pourcentFalse = 100 - pourcentTrue
                stats[champ] = {
                    'type': 'boolean',
                    'pourcentTrue': pourcentTrue,
                    'pourcentFalse': pourcentFalse
                }
                continue
            
            lengthList = [len(s[champ]) for s in structure if is_list(s[champ])]
            if lengthList:
                stats[champ] = {
                    'type': 'liste',
                    'min': min(lengthList),
                    'max': max(lengthList),
                    'moyenne': sum(lengthList) / len(lengthList)
                }
            
    
    for champ, values in stats.items():
        print(f"Champ : {champ}")
        if values['type'] == 'numerique':
            print(f"  Type : {values['type']}")
            print(f"  Min : {values['min']}")
            print(f"  Max : {values['max']}")
            print(f"  Moyenne : {values['moyenne']}")
        elif values['type'] == 'boolean':
            print(f"  Type : {values['type']}")
            print(f"  Pourcentage de vrai : {values['pourcentTrue']}%")
            print(f"  Pourcentage de faux : {values['pourcentFalse']}%")
        elif values['type'] == 'liste':
            print(f"  Type : {values['type']}")
            print(f"  Taille min : {values['min']}")
            print(f"  Taille max : {values['max']}")
            print(f"  Taille moyenne : {values['moyenne']}")