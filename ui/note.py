import datetime 

class Note():
    __count = 0
    def __init__(self, title, note_body, date_of_creation, id = None):
        if id == None:
            Note.__count += 1
            self.__id = Note.__count
        else:
            if Note.__count < id:
                Note.__count = id
            self.__id = id
        self.__title = title
        self.__note_body = note_body 
        self.__date_of_creation = date_of_creation 

    def get_id(self):
        return self.__id

    def set_title(self, title):
        self.__title = title
        self.__date_of_creation = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")

    def get_title(self):
        return self.__title

    def set_note_body(self, note_body):
        self.__note_body = note_body
        self.__date_of_creation = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")

    def get_note_body(self):
        return self.__note_body
    
    def get_date(self):
        return self.__date_of_creation

    def display_info(self):
        return '\t{\n'+f' \
            "id":               {self.__id}\n \
            "title":            {self.__title}\n \
            "note_body":        {self.__note_body}\n \
            "date_of_creation": {self.__date_of_creation}\n'+'\t}\n'