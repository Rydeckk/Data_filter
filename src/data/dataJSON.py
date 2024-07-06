import json

def save_data_json(file):
    with open(file,'r') as jsonFile:
        return json.load(jsonFile)
    
def create_file_json(structure):
    with open("export/data.json",'w') as jsonFile:
        json.dump(structure, jsonFile, indent=4)