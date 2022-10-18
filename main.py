import names


def name():
    a = names.get_first_name()
    return a


def surname():
    b = names.get_last_name()
    return b


Pers_name = name()
Pers_surname = surname()
print(f'My name is {Pers_name} {Pers_surname}')
