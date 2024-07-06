import csv
from utils.utils import cast_value

def save_data_csv(file):
    with open(file, 'r') as csvFile:
        dictReader = csv.DictReader(csvFile,delimiter=";")
        data = []
        for row in dictReader:
            casted_row = {key: cast_value(value) for key, value in row.items()}
            data.append(casted_row)
        return data
    
def create_file_csv(structure):
    keys = structure[0].keys()
    with open("export/data.csv", 'w', newline='') as csvFile:
        dict_writer = csv.DictWriter(csvFile, fieldnames=keys, delimiter=";")
        dict_writer.writeheader()
        dict_writer.writerows(structure)