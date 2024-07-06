import ast

def cast_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            try: 
                return ast.literal_eval(value)
            except (ValueError, SyntaxError):
                return value