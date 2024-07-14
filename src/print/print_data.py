def print_data(structure):
    for dict in structure:
        print("Ligne : ")
        for key, value in dict.items():
            print(f"\t{key} : {value}")
        print("\n")