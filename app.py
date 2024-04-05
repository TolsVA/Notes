import os
from view.menu import start_menu
from ui.comands import *
from ui.init import init_menu

class App():
    if os.path.exists('db') == False:
        os.mkdir('db')
    print(f'Вы открыли приложение заметки. Допустимые команды {[com.name for com in Command]}')
    start_menu(init_menu())