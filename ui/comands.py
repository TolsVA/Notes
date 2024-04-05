from enum import Enum

class Command(Enum):
    ADD_NOTE = 'add_note'
    UPDATE_NOTE = 'update_note'
    DELIT_NOTE = 'delit_note'
    DELIT_ALL = 'delit_all'
    SHOW_NOTE = 'show_note'
    SORT_BY_DATE = 'sort_by_date'
    EXIT = 'exit'