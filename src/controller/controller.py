from data.dataCSV import create_file_csv, save_data_csv
from data.dataJSON import create_file_json, save_data_json
from data.dataXML import create_file_xml, save_data_xml
from data.dataYAML import create_file_yaml, save_data_yaml
from PyQt5.QtWidgets import QTableWidgetItem, QLabel

from filter.filter_data import filter_data
from utils.utils import is_boolean, is_list, is_numeric

class Controller:
    def __init__(self, model):
        self.model = model

    def save_data(self,name_file):
        fileExtension = name_file.split(".")[-1]

        if(fileExtension == "csv"):
            self.model.structure = save_data_csv(name_file)
        elif(fileExtension == "json"):
            self.model.structure = save_data_json(name_file)
        elif(fileExtension == "xml"):
            self.model.structure = save_data_xml(name_file)
        elif(fileExtension == "yaml"):
            self.model.structure = save_data_yaml(name_file)
        else:
            raise TypeError

    def get_number_row(self):
        return len(self.model.structure)
    
    def get_number_column(self):
        maxLength = 0
        for item in self.model.structure:
            if maxLength < len(item.keys()):
                maxLength = len(item.keys())
        return maxLength
    
    def fill_table(self, table):
        nbRow = 0
        for item in self.model.structure:
            nbColumn = 0
            if(nbRow == 0):
                for key in item.keys():
                    cell = QTableWidgetItem(key)
                    table.setItem(nbRow, nbColumn, cell)
                    nbColumn += 1
                nbRow += 1
            nbColumn = 0
            for key in item.keys():
                if(isinstance(item[key], list)):
                    convertStr = [str(i) for i in item[key]]
                    listToString = ", ".join(convertStr)
                    cell = QTableWidgetItem(listToString)
                else:
                    cell = QTableWidgetItem(str(item[key]))
                table.setItem(nbRow, nbColumn, cell)
                nbColumn += 1
            nbRow += 1
    
    def export_data(self, format):
        if(format == "csv"):
            create_file_csv(self.model.structure)
        elif(format == "json"):
            create_file_json(self.model.structure)
        elif(format == "xml"):
            create_file_xml(self.model.structure)
        elif(format == "yaml"):
            create_file_yaml(self.model.structure)
        else:
            raise TypeError
        
    def get_stats(self, grid):
        stats = {}
        for ligne in self.model.structure:
            for champ in ligne:
                valeursNum = [s[champ] for s in self.model.structure if is_numeric(s[champ])]
                if valeursNum:
                    stats[champ] = {
                        'type': 'numerique',
                        'min': min(valeursNum),
                        'max': max(valeursNum),
                        'moyenne': sum(valeursNum) / len(valeursNum)
                    }
                    continue

                valeursBool = [s[champ] for s in self.model.structure if is_boolean(s[champ])]
                if valeursBool:
                    pourcentTrue = sum(valeursBool) / len(valeursBool) * 100
                    pourcentFalse = 100 - pourcentTrue
                    stats[champ] = {
                        'type': 'boolean',
                        'pourcentTrue': pourcentTrue,
                        'pourcentFalse': pourcentFalse
                    }
                    continue
                
                lengthList = [len(s[champ]) for s in self.model.structure if is_list(s[champ])]
                if lengthList:
                    stats[champ] = {
                        'type': 'liste',
                        'min': min(lengthList),
                        'max': max(lengthList),
                        'moyenne': sum(lengthList) / len(lengthList)
                    }
                
        x = 0
        y = 0
        for champ, values in stats.items():
            text = f"Champ : {champ} \n"
            if values['type'] == 'numerique':
                text += f"  Type : {values['type']} \n"
                text += f"  Min : {values['min']} \n"
                text += f"  Max : {values['max']} \n"
                text += f"  Moyenne : {values['moyenne']} \n"
                labStat = QLabel(text)
                y += 1
            elif values['type'] == 'boolean':
                text += f"  Type : {values['type']} \n"
                text += f"  Pourcentage de vrai : {values['pourcentTrue']}% \n"
                text += f"  Pourcentage de faux : {values['pourcentFalse']}% \n"
                labStat = QLabel(text)
                y += 1
            elif values['type'] == 'liste':
                text += f"  Type : {values['type']} \n"
                text += f"  Taille min : {values['min']} \n"
                text += f"  Taille max : {values['max']} \n"
                text += f"  Taille moyenne : {values['moyenne']} \n"
                labStat = QLabel(text)
                y += 1
            labStat.setStyleSheet("border: 2px solid black; font-size: 14px;")
            grid.addWidget(labStat,x,y)

            if(y % 3 == 0 and y != 0):
                x += 1
                y = 0

    def sort_data(self, fields, order):
        reverse = (order == "desc")
        self.model.structure = sorted(self.model.structure, key=lambda x: tuple(x.get(field) for field in fields), reverse=reverse)

    def filter_data(self, field, operator, valueToCompare):
        self.model.structure = filter_data(self.model.structure, field, operator, valueToCompare)