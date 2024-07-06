from data.dataCSV import create_file_csv, save_data_csv
from data.dataJSON import create_file_json, save_data_json
from data.dataXML import create_file_xml, save_data_xml
from data.dataYAML import create_file_yaml, save_data_yaml


structure = []

name_file = input("Rentrez le chemin du fichier : ")

fileExtension = name_file.split(".")[-1]

if(fileExtension == "csv"):
    structure = save_data_csv(name_file)
elif(fileExtension == "json"):
    structure = save_data_json(name_file)
elif(fileExtension == "xml"):
    structure = save_data_xml(name_file)
elif(fileExtension == "yaml"):
    structure = save_data_yaml(name_file)
else:
    print("Mauvaise extension de fichier")


print(structure)

choice = input("Export en quel format : ")

if(choice == "csv"):
    create_file_csv(structure)
elif(choice == "json"):
    create_file_json(structure)
elif(choice == "xml"):
    create_file_xml(structure)
elif(choice == "yaml"):
    create_file_yaml(structure)
else:
    print("Mauvais format")