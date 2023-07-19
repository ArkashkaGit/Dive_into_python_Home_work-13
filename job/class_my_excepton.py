class PersonException(Exception):
    pass


class PersonNameException(PersonException):
    def __init__(self):
        pass

    def __str__(self):
        return f'Имя и Фамилия не могут превышать заданный лимит и могуть быть только в строковом представлении'


class PersonAgeException(PersonException):
    def __init__(self):
        pass

    def __str__(self):
        return f'Возраст не может быть отритцательным числом и не может превышать отметку 130 лет!'
