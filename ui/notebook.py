class Notebook():
    def __init__(self, notes = list()):
        self.__notes = notes
    
    def set_notes(self, note):
        self.__notes.append(note)

    def get_notes(self):
        return self.__notes
    
    def delit_all(self):
        self.__notes = list()

    def display_info(self):
        print('{\n  "notes": [')
        for note in self.__notes:
            print(note.display_info())
        print('    ]\n}')