from ui.note import *
import datetime
from exc.exception import *

class Manager():
    def create_note(self):
        title = input('Введите заголовок заметки: ')
        note_body = input('Введите текст заметки: ')
        return Note(title, note_body, datetime.datetime.today().strftime("%d.%m.%Y %H:%M"))
    
    def select_note(self, notebook):
        id = input('Выбери заметку по индексу: ')
        list_id = [str(note.get_id()) for note in notebook.get_notes()]
        while id not in list_id:
            print(f'Вы ввели {id}. Такого индекса нет вот список возможных {[int(id) for id in list_id]}: ')
            id = input('Выбери заметку по индексу: ')

        for note in notebook.get_notes():
            if id == str(note.get_id()):
                return note
            
    def edit_note(self, note):
        title = input(f'Заголовок: {note.get_title()} введите новое название или проигнарируйте: ')
        if len(title) > 0:
            note.set_title(title)

        note_body = input(f'Текст заметки: {note.get_note_body()} введите новый текст или проигнарируйте: ')
        if len(note_body) > 0:
            note.set_note_body(note_body)

        return note
    def date_range(self, notebook):
        list_date = list(note.get_date().split(' ') for note in notebook.get_notes())
        list_date = list(date[0].split('.') for date in list_date)
        list_date = list(datetime.datetime(int(date[2]), int(date[1]), int(date[0])) for date in list_date)
        
        date_min = datetime.datetime(2100, 1, 1)
        date_max = datetime.datetime(2000, 1, 1)

        for date in list_date:
            if date_min > date: date_min = date
            if date_max < date: date_max = date

        print(f'Диапазон по датам ваших заметок: {[date_min, date_max]}')

        date_start = self.get_date(f'Введите дату начала в формате дд.мм.гггг в диапазоне {[date_min.year, date_max.year]}: ', date_min.year, date_max.year)
        date_end = self.get_date(f'Введите дату конца в формате дд.мм.гггг в диапазоне {[date_min.year, date_max.year]}: ', date_min.year, date_max.year)

        try:
            date_start = datetime.datetime(int(date_start[0]), int(date_start[1]), int(date_start[2]))
            date_end = datetime.datetime(int(date_end[0]), int(date_end[1]), int(date_end[2]))
        except TypeError as e:
            print(f'Непредвиденная ошибка {e}')
            self.date_range(notebook)

        list_result = list()

        for i in range(len(list_date)):
            if list_date[i] >= date_start and list_date[i] <= date_end:
                list_result.append(notebook.get_notes()[i].display_info())

        for note in list_result:
            print(note)
    
    def get_date(self, message, year_min, year_max):
        try:
            str_date = input(message)
            str_date = str_date.split('.')
            if len(str_date) != 3:
                raise WrongLengthException('Не верный обьем данных введите дату в формате дд.мм.гггг: ')
            
            day = self.get_value(str_date[0], f'Вы ввели {str_date[0]}. Не верное приведение типа день должен быть числом: ')
            if day < 1 or day > 31:
                raise InvalidDay('Не верно указан день выбери из диапазона от 1 до 28(31): ')
            
            month = self.get_value(str_date[1], f'Вы ввели {str_date[1]}. Не верное приведение типа месяц должен быть числом: ')
            if month < 1 or month > 12:
                raise InvalidMonth('Не верно указан месяц выбери из диапазона от 1 до 12: ')
            
            year = self.get_value(str_date[2], f'Вы ввели {str_date[2]}. Не верное приведение типа гол должен быть числом: ')
            if year < year_min or year > year_max:
                raise YearIsIncorrect(f'не верно указан год выбери из диапазона от {year_min} до {year_max}: ')
            
            return [int(year), int(month), int(day)]
        except (WrongLengthException, YearIsIncorrect, InvalidMonth, InvalidDay, MyValueError) as e:
            print(e)
            self.get_date(message, year_min, year_max)

    def get_value(self, value, message):
        try:
            day = int(value)
            return day
        except(ValueError) as e:
            raise MyValueError(message)