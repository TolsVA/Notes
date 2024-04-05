from ui.comands import *
from ui.presenter import *
from ui.notebook import *

presenter = Presenter
notebook = Notebook

def start_menu(new_notebook):
    global notebook
    notebook = new_notebook
    while True:
        command = input('Введите команду: ').upper()
        while command not in [com.name for com in Command]:
            print(f'Вы ввели {command} допустимые команды {[com.name for com in Command]}')
            command = input('Введите команду: ').upper()
        
        for com in Command:
            if com.name == command:
                if command == 'EXIT':
                    return
                globals()[com.value]()

def add_note():
    notebook.set_notes(presenter.add_note())
    save_all()

def update_note(): 
    presenter.update_note(notebook)
    save_all()

def delit_note(): 
    presenter.delit_note(notebook)
    save_all()

def delit_all(): 
    presenter.delit_all(notebook)
    save_all()

def show_note(): presenter.show_note(notebook)

def sort_by_date(): presenter.sort_by_date(notebook)

def save_all():
    presenter.save_all(notebook)
    if len(notebook.get_notes()) == 0:
        print('У вас нет заметок')
    else:
        notebook.display_info()