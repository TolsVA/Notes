from database.database import *
from ui.console import *

database = Database()
console_manage = Manager()
class Presenter():

    def add_note():
        return console_manage.create_note()

    def save_all(notebook):
        database.save_all(notebook)

    def update_note(notebook):
        note = console_manage.select_note(notebook)
        note = console_manage.edit_note(note)

    def delit_note(notebook):
        note = console_manage.select_note(notebook)
        list_notes = notebook.get_notes()
        list_notes.remove(note)

    def delit_all(notebook):
        notebook.delit_all()

    def show_note(notebook):
        note = console_manage.select_note(notebook)
        print(f'Ваша заметка: {note.display_info()}')

    def sort_by_date(notebook):
        console_manage.date_range(notebook)

    def init_menu():
        return database.init_menu()