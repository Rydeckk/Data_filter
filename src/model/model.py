class Model:
    def __init__(self):
        self._structure = []
    
    def _get_structure(self):
        return self._structure
    
    def _set_structure(self, newStruct):
        self._structure = newStruct

    structure = property(_get_structure, _set_structure)