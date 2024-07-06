import yaml

def save_data_yaml(file):
    with open(file, 'r') as yamlFile:
        return yaml.safe_load(yamlFile)
    
def create_file_yaml(structure):
    with open("export/data.yaml",'w') as yamlFile:
        yaml.dump(structure, yamlFile)