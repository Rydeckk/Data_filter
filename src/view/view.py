from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QStackedWidget, QGridLayout
from enum import Enum

class LayoutOrder(Enum):
    IMPORT = 0
    MENU = 1
    FILTRE = 2
    TRI = 3
    STATS = 4
    EXPORT = 5
    AFFICHER = 6

class MainWindow(QMainWindow):
    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.setWindowTitle("Data_filter")
        self.setGeometry(600, 200, 600, 400)

        self.widgetCentral = QWidget(self)
        self.setCentralWidget(self.widgetCentral)

        self.mainLayout = QVBoxLayout(self.widgetCentral)

        self.buttonReturnMenu = QPushButton("Retour au menu")
        self.buttonReturnMenu.clicked.connect(self.click_return_menu)

        self.stackedWidget = QStackedWidget()
        self.mainLayout.addWidget(self.stackedWidget)

        self.layoutImport = LayoutImport(self.controller, self.layout_to_show)
        self.layoutMenu = LayoutMenu(self.controller, self.layout_to_show)
        self.stackedWidget.addWidget(self.layoutImport)
        self.stackedWidget.addWidget(self.layoutMenu)
        self.stackedWidget.setCurrentIndex(LayoutOrder.IMPORT.value)

        self.layout_to_show("import")

        self.mainLayout.addWidget(self.buttonReturnMenu)

    def layout_to_show(self, name):
        if(name == "import"):
            self.currentLayout = self.layoutImport
            self.buttonReturnMenu.setHidden(True)
        elif(name == "menu"):
            self.clear_stacked_widget()

            self.layoutFiltre = LayoutFiltre(self.controller, self.layout_to_show)
            self.layoutTri = LayoutTri(self.controller, self.layout_to_show)
            self.layoutStats = LayoutStats(self.controller, self.layout_to_show)
            self.layoutExport = LayoutExport(self.controller, self.layout_to_show)
            self.layoutAfficher = LayoutAfficher(self.controller, self.layout_to_show)

            self.stackedWidget.addWidget(self.layoutFiltre)
            self.stackedWidget.addWidget(self.layoutTri)
            self.stackedWidget.addWidget(self.layoutStats)
            self.stackedWidget.addWidget(self.layoutExport)
            self.stackedWidget.addWidget(self.layoutAfficher)

            self.stackedWidget.setCurrentIndex(LayoutOrder.MENU.value)
            self.currentLayout = self.layoutMenu
            self.buttonReturnMenu.setHidden(True)
        elif(name == "filtre"):
            self.currentLayout = self.layoutFiltre
            self.stackedWidget.setCurrentIndex(LayoutOrder.FILTRE.value)
            self.buttonReturnMenu.setHidden(False)
        elif(name == "tri"):
            self.currentLayout = self.layoutTri
            self.stackedWidget.setCurrentIndex(LayoutOrder.TRI.value)
            self.buttonReturnMenu.setHidden(False)
        elif(name == "stats"):
            self.currentLayout = self.layoutStats
            self.stackedWidget.setCurrentIndex(LayoutOrder.STATS.value)
            self.buttonReturnMenu.setHidden(False)
        elif(name == "export"):
            self.currentLayout = self.layoutExport
            self.stackedWidget.setCurrentIndex(LayoutOrder.EXPORT.value)
            self.buttonReturnMenu.setHidden(False)
        elif(name == "afficher"):
            self.currentLayout = self.layoutAfficher
            self.stackedWidget.setCurrentIndex(LayoutOrder.AFFICHER.value)
            self.buttonReturnMenu.setHidden(False)

    def click_return_menu(self):
        self.layout_to_show("menu")

    def clear_stacked_widget(self):
        while self.stackedWidget.count() > 2:
            widget_to_remove = self.stackedWidget.widget(2)
            self.stackedWidget.removeWidget(widget_to_remove)

class LayoutImport(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback
        
        self.buttonSaveImport = QPushButton("Sauvegarder")
        self.buttonSaveImport.clicked.connect(self.click_button_save)
        self.tbNameFile = QLineEdit()
        self.tbNameFile.setPlaceholderText("Rentrez un nom de fichier (csv, json, xml, yaml)")
        self.tbNameFile.setFixedSize(300,30)
        self.labError = QLabel()
        self.labError.setHidden(True)
        self.labError.setStyleSheet("color: red;")
        
        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)
        layout.addWidget(self.tbNameFile)
        layout.addWidget(self.labError)
        layout.addSpacing(20)
        layout.addWidget(self.buttonSaveImport)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        
        mainLayout.addItem(horizontalSpacer)
        
        self.setMaximumSize(600,400)

    def click_button_save(self):
        try:
            self.controller.save_data(self.tbNameFile.text())
            self.labError.setText("")
            self.layout_to_show_callback("menu")
            self.labError.setHidden(True)
        except OSError:
            self.labError.setText("Fichier introuvable")
            self.labError.setHidden(False)
        except TypeError:
            self.labError.setText("Mauvaise extension, il doit être du format (csv, json, xml, yaml)")
            self.labError.setHidden(False)


class LayoutMenu(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        labelMenu = QLabel("Choisissez une option")
        labelMenu.setStyleSheet("font-size: 16px;")
        self.buttonFiltre = QPushButton("Filtre")
        self.buttonFiltre.setFixedSize(200,30)
        self.buttonTri = QPushButton("Tri")
        self.buttonTri.setFixedSize(200,30)
        self.buttonStats = QPushButton("Stats")
        self.buttonStats.setFixedSize(200,30)
        self.buttonExport = QPushButton("Export")
        self.buttonExport.setFixedSize(200,30)
        self.buttonAfficher = QPushButton("Afficher")
        self.buttonAfficher.setFixedSize(200,30)

        self.buttonFiltre.clicked.connect(self.click_button_filtre)
        self.buttonTri.clicked.connect(self.click_button_tri)
        self.buttonStats.clicked.connect(self.click_button_stats)
        self.buttonExport.clicked.connect(self.click_button_export)
        self.buttonAfficher.clicked.connect(self.click_button_afficher)

        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)
        layout.addWidget(labelMenu)
        layout.addSpacing(20)
        layout.addWidget(self.buttonFiltre)
        layout.addSpacing(5)
        layout.addWidget(self.buttonTri)
        layout.addSpacing(5)
        layout.addWidget(self.buttonStats)
        layout.addSpacing(5)
        layout.addWidget(self.buttonExport)
        layout.addSpacing(5)
        layout.addWidget(self.buttonAfficher)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        
        mainLayout.addItem(horizontalSpacer)
        
        self.setMinimumSize(600,400)

    def click_button_filtre(self):
        self.layout_to_show_callback("filtre")
    
    def click_button_tri(self):
        self.layout_to_show_callback("tri")
    
    def click_button_stats(self):
        self.layout_to_show_callback("stats")

    def click_button_export(self):
        self.layout_to_show_callback("export")

    def click_button_afficher(self):
        self.layout_to_show_callback("afficher")


class LayoutFiltre(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tbChamp = QLineEdit()
        self.tbChamp.setPlaceholderText("Entrez le champs à filtrer")
        self.tbChamp.setFixedHeight(30)

        self.tbOperator = QLineEdit()
        self.tbOperator.setPlaceholderText("Rentrez un opérateur")
        self.tbOperator.setFixedHeight(30)                     

        self.tbValueToCompare = QLineEdit()
        self.tbValueToCompare.setPlaceholderText("Entrez la valeur de comparaison")
        self.tbValueToCompare.setFixedHeight(30)

        self.buttonFiltrer = QPushButton("Filtrer")
        self.buttonFiltrer.clicked.connect(self.click_button_filter)

        labOperateur = QLabel("(==, !=, >, >=, <, <=, contient, commence_par, finit_par, tous_les_elements, min, max, moyenne)")

        self.labSuccess = QLabel("Données filtrées avec succès")
        self.labSuccess.setHidden(True)
        self.labSuccess.setStyleSheet("color: green;")

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)
        layout.addWidget(self.tbChamp)
        layout.addSpacing(5)
        layout.addWidget(self.tbOperator)
        layout.addWidget(labOperateur)
        layout.addSpacing(5)
        layout.addWidget(self.tbValueToCompare)
        layout.addSpacing(20)
        layout.addWidget(self.buttonFiltrer)
        layout.addWidget(self.labSuccess)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        
        mainLayout.addItem(horizontalSpacer)

    def click_button_filter(self):
        self.controller.filter_data(self.tbChamp.text(), self.tbOperator.text(), self.tbValueToCompare.text())
        self.labSuccess.setHidden(False)

class LayoutTri(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tbchamp = QLineEdit()
        self.tbchamp.setPlaceholderText("Entrez les champs à trier (séparé par des virgules)")
        self.tbchamp.setFixedSize(300,30)

        self.tbOrder = QLineEdit()
        self.tbOrder.setPlaceholderText("Entrez l'ordre du tri (asc/desc)")
        self.tbOrder.setFixedSize(300,30)

        self.buttonTri = QPushButton("Trier")
        self.buttonTri.clicked.connect(self.click_button_tri)

        self.labSuccess = QLabel("Données triées avec succès")
        self.labSuccess.setHidden(True)
        self.labSuccess.setStyleSheet("color: green;")

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)
        layout.addWidget(self.tbchamp)
        layout.addSpacing(5)
        layout.addWidget(self.tbOrder)
        layout.addSpacing(20)
        layout.addWidget(self.buttonTri)
        layout.addWidget(self.labSuccess)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        
        mainLayout.addItem(horizontalSpacer)

    def click_button_tri(self):
        self.controller.sort_data(self.tbchamp.text().split(","), self.tbOrder.text())
        self.labSuccess.setHidden(False)

class LayoutStats(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        mainLayout = QHBoxLayout(self)

        self.gridStat = QGridLayout()
        self.controller.get_stats(self.gridStat)

        layout = QVBoxLayout()
        layout.addLayout(self.gridStat)

        mainLayout.addLayout(layout)

class LayoutExport(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tbExtensionExport = QLineEdit()
        self.tbExtensionExport.setPlaceholderText("Rentrez le format que vous voulez (csv, json, xml, yaml)")
        self.tbExtensionExport.setFixedSize(300,30)

        self.buttonExport = QPushButton("Exporter")
        self.buttonExport.clicked.connect(self.click_export)

        self.labError = QLabel("Mauvais format")
        self.labError.setHidden(True)
        self.labError.setStyleSheet("color: red;")

        self.labSuccess = QLabel("Export Réussi !")
        self.labSuccess.setHidden(True)
        self.labSuccess.setStyleSheet("color: green;")

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)
        layout.addWidget(self.tbExtensionExport)
        layout.addWidget(self.labError)
        layout.addWidget(self.labSuccess)
        layout.addSpacing(20)
        layout.addWidget(self.buttonExport)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        mainLayout.addItem(horizontalSpacer)

    def click_export(self):
        try:
            self.controller.export_data(self.tbExtensionExport.text())
            self.labError.setHidden(True)
            self.labSuccess.setHidden(False)
        except TypeError:
            self.labError.setHidden(False)
            self.labSuccess.setHidden(True)


class LayoutAfficher(QWidget):
    def __init__(self, controller, layout_to_show_callback):
        super().__init__()
        self.controller = controller
        self.layout_to_show_callback = layout_to_show_callback

        mainLayout = QHBoxLayout(self)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        mainLayout.addItem(horizontalSpacer)

        layout = QVBoxLayout()
        layout.addItem(verticalSpacer)

        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumSize(600,400)

        nbColumn = self.controller.get_number_column()
        nbRow = self.controller.get_number_row() + 1
        self.tableWidget.setRowCount(nbRow)
        self.tableWidget.setColumnCount(nbColumn)
        self.controller.fill_table(self.tableWidget)

        layout.addWidget(self.tableWidget)
        layout.addItem(verticalSpacer)

        mainLayout.addLayout(layout)
        mainLayout.addItem(horizontalSpacer)
        
