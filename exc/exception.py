class WrongLengthException(Exception):
    def __init__(self, text):
        super().__init__(text)

class YearIsIncorrect(Exception):
    def __init__(self, text):
        super().__init__(text)

class InvalidMonth(Exception):
    def __init__(self, text):
        super().__init__(text)

class InvalidDay(Exception):
    def __init__(self, text):
        super().__init__(text)

class MyValueError(ValueError):
    def __init__(self, text):
        super().__init__(text)