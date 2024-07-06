from lxml import etree as ET
from utils.utils import cast_value

def save_data_xml(file):
    with open(file, 'r') as xmlFile:
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        data = []
        for item in root.findall("item"):
            items = {}
            for element in item:
                if list(element):
                    items[element.tag] = [cast_value(e.text) for e in element]
                else:
                    items[element.tag] = cast_value(element.text)
            data.append(items)
        
        return data
    
def create_file_xml(structure):
    root = ET.Element('structure')
    with open("export/data.xml",'wb') as xmlFile:
        for row in structure:
            item = ET.SubElement(root,'item')
            for key, value in row.items():
                if isinstance(value, list):
                    list_element = ET.SubElement(item, key)
                    for i in value:
                        item_element = ET.SubElement(list_element, key + "Element")
                        item_element.text = str(i)
                else:
                    element = ET.SubElement(item, key)
                    element.text = str(value)
        tree = ET.ElementTree(root)
        xmlFile.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(xmlFile, encoding='utf-8', pretty_print=True, xml_declaration=False)
