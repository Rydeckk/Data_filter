from controller.controller import Controller
from data.dataCSV import create_file_csv, save_data_csv
from data.dataJSON import create_file_json, save_data_json
from data.dataXML import create_file_xml, save_data_xml
from data.dataYAML import create_file_yaml, save_data_yaml
from model.model import Model
from print.print_data import print_data
from stats.stats import print_structure_stats
from filter.filter_data import filter_data
from sort.sort_data import sort_data
import time
import sys
from PyQt5.QtWidgets import QApplication

from view.view import MainWindow

structure = []

choiceApp = ""

while(choiceApp != "menu" and choiceApp != "ig" and choiceApp != "quitter"):
    print(choiceApp)
    print("Vous devez taper ce qu'il y a entre par parenthèse pour y accéder !")
    print("Menu (menu)")
    print("Interface graphique (ig)")
    print("Quitter le programme (quitter)")
    choiceApp = input()


if(choiceApp == "menu"):
    fileExtension = ""
    error = False

    while((fileExtension != "csv" and fileExtension != "json" and fileExtension != "xml" and fileExtension != "yaml") or error == True):
        name_file = input("Rentrez le chemin du fichier pour importer les données (csv, json, xml, yaml) : \n")

        fileExtension = name_file.split(".")[-1]

        if(fileExtension == "csv"):
            try:
                structure = save_data_csv(name_file)
                error = False
            except OSError:
                print("Fichier introuvable")
                error = True
        elif(fileExtension == "json"):
            try:
                structure = save_data_json(name_file)
                error = False
            except OSError:
                print("Fichier introuvable")
                error = True
        elif(fileExtension == "xml"):
            try:
                structure = save_data_xml(name_file)
                error = False
            except OSError:
                print("Fichier introuvable")
                error = True
        elif(fileExtension == "yaml"):
            try:
                structure = save_data_yaml(name_file)
                error = False
            except OSError:
                print("Fichier introuvable")
                error = True
        else:
            print("Mauvaise extension, il doit être du format (csv, json, xml, yaml)")

    menuChoice = ""

    while(menuChoice != "quitter"):
        print("Menu :")
        print(" - Filtrer les données (filtre)")
        print(" - Trier les données (tri)")
        print(" - Afficher statistiques (stats)")
        print(" - Export données (export)")
        print(" - afficher la structure (afficher)")
        print(" - Quitter (quitter)")
        menuChoice = input()
        print("\n")

        if(menuChoice == "filtre"):
            field = input("Entrez le champs à filtrer : \n")
            print("\n")
            operator = input("Entre l'operateur de comparaisaon (==, !=, >, >=, <, <=, contient, commence_par, finit_par, tous_les_elements, min, max, moyenne) : \n")
            print("\n")
            value = input("Entrez la valeur de comparaison : \n")
            structure = filter_data(structure, field, operator, value)
            print("Données filtrées :")
            print(structure)
            time.sleep(5)
        elif(menuChoice == "tri"):
            fields = input("Entrez les champs à trier (séparé par des virgules) : \n").split(',')
            print("\n")
            order = input("Entrez l'ordre du tri (asc/desc) : \n")
            reverse = (order == "desc")
            structure = sort_data(structure, fields, reverse)
            print("Données triées :")
            print(structure)
            time.sleep(5)
        elif(menuChoice == "stats"):
            print_structure_stats(structure)
            print("\n")
            time.sleep(5)
        elif(menuChoice == "export"):
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
            time.sleep(5)
        elif(menuChoice == "afficher"):
            print_data(structure)
            time.sleep(5)
        elif(menuChoice == "quitter"):
            print("\n")
            print("Bye !")
            break
        else:
            print("Mauvais choix !")
            print("\n")
elif(choiceApp == "ig"):
    model = Model()
    controller = Controller(model)
    app = QApplication.instance() 
    if not app: 
        app = QApplication(sys.argv)

    fen = MainWindow(controller)
    fen.show()

    fen.raise_()
    fen.activateWindow()

    app.exec_()
elif(choiceApp == "quitter"):
    print("Bye !")
else:
        print("Mauvais choix")
