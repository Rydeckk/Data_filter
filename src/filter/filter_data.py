
def filter_data(structure, field, operator, value):
    filtered_data = []
    try:
        value = float(value)
    except ValueError:
        pass  

    for row in structure:
        if field in row:
            if isinstance(row[field], int):
                if operator == "==":
                    if row[field] == value:
                        filtered_data.append(row)
                elif operator == "!=":
                    if row[field] != value:
                        filtered_data.append(row)
                elif operator == "<=":
                    if row[field] < value:
                        filtered_data.append(row)
                elif operator == ">=":
                    if row[field] > value:
                        filtered_data.append(row)
            
            elif isinstance(row[field], str):
                if operator == "contient":
                    if value in row[field]:
                        filtered_data.append(row)
                elif operator == "commence_par":
                    if row[field].startswith(value):
                        filtered_data.append(row)
                elif operator == "finit_par":
                    if row[field].endswith(value):
                        filtered_data.append(row)

            elif isinstance(row[field], bool):
                if operator == "==":
                    if value == row[field]:
                        filtered_data.append(row) 

            elif isinstance(row[field], list):
                list_length = len(row[field])
                if operator == "==":
                    if list_length == value:
                        filtered_data.append(row)
                elif operator == "!=":
                    if list_length != value:
                        filtered_data.append(row)
                elif operator == "<":
                    if list_length < value:
                        filtered_data.append(row)
                elif operator == "<=":
                    if list_length <= value:
                        filtered_data.append(row)
                elif operator == ">":
                    if list_length > value:
                        filtered_data.append(row)
                elif operator == ">=":
                    if list_length >= value:
                        filtered_data.append(row)
                elif operator == "tous_les_elements":
                    if all(element == value for element in row[field]):
                        filtered_data.append(row)
                elif operator == "min":
                    if isinstance(min(row[field]), (int, float)) and min(row[field]) == value:
                        filtered_data.append(row)
                elif operator == "max":
                    if isinstance(max(row[field]), (int, float)) and max(row[field]) == value:
                        filtered_data.append(row)
                elif operator == "moyenne":
                    if all(isinstance(item, (int, float)) for item in row[field]):
                        if (sum(row[field]) / len(row[field])) == value:
                            filtered_data.append(row)
    return filtered_data


