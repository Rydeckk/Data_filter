def sort_data(structure, fields, reverse = False):
    return sorted(structure, key=lambda x: tuple(x.get(field) for field in fields), reverse=reverse)
