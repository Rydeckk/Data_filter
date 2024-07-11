from data.dataCSV import create_file_csv, save_data_csv
from data.dataJSON import create_file_json, save_data_json
from data.dataXML import create_file_xml, save_data_xml
from data.dataYAML import create_file_yaml, save_data_yaml
from stats.stats import print_structure_stats
from filter.filter_data import filter_data
from sort.sort_data import sort_data


structure = []

name_file = input("Rentrez le chemin du fichier : \n")

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

print("\n")
print(structure)
print("\n")
print_structure_stats(structure)
print("\n")

filterYes = input("Voulez-vous filtrer des données ? (yes/no) : \n")
if filterYes == "yes":
    field = input("Entrez le champs à filtrer : \n")
    print("\n")
    operator = input("Entre l'operateur de comparaisaon (==, !=, >, >=, <, <=, contient, commence_par, finit_par, tous_les_elements, min, max, moyenne) : \n")
    print("\n")
    value = input("Entrez la valeur de comparaison : \n")
    structure = filter_data(structure, field, operator, value)
    print("Données filtrées :")
    print(structure)

print("\n")
sortYes = input("Voulez-vous trier les données ? (yes/no) : \n")
if sortYes == "yes" :
    fields = input("Entrez les champs à trier (séparé par des virgules) : \n").split(',')
    print("\n")
    order = input("Entrez l'ordre du tri (asc/desc) : \n")
    reverse = (order == "desc")
    structure = sort_data(structure, fields, reverse)
    print("Données triées :")
    print(structure)

print("\n")
exportYes = input("Voulez vous exporter les données ? (yes/no) : \n")
if(exportYes == "yes"):
    choice = input("Export en quel format : \n")
    print("\n")
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