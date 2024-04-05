import os
import json
from ui.note import *
from ui.notebook import *

class Database():
    def save_all(self, notebook):
        new_list = list(note.__dict__ for note in notebook.get_notes())
        new_notebook = Notebook(new_list)
        
        with open('db/notes.json', 'w', encoding='utf-8') as file:
              json.dump(new_notebook.__dict__, file, indent = 4)

    def init_menu(self):
        notebook = Notebook()

        if os.path.exists('db/notes.json') == False:
            with open('db/notes.json', 'w', encoding='utf-8') as file:
                json.dump(notebook.__dict__, file, indent = 4)

        with open('db/notes.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

        list_1 = data['_Notebook__notes']
        list_note = list()
        for note_dict in list_1:
            note = Note(note_dict['_Note__title'], note_dict['_Note__note_body'], note_dict['_Note__date_of_creation'], note_dict['_Note__id'])
            list_note.append(note)

        notebook2 = Notebook(list_note)
        if len(list_note) == 0:
            print('Список ваших заметок пуст')
        else:
            print('Список ваших заметок')
            notebook2.display_info()

        return notebook2