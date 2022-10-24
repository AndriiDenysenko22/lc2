import names


def name():
    a = names.get_first_name()
    return a


def surname():
    b = names.get_last_name()
    return b


def friend():
    c = names.get_full_name()
    return c


Pers_name = name()
Pers_surname = surname()
friend_of_mine = friend()
print(f'My name is {Pers_name} {Pers_surname}. I have a friend - {friend_of_mine}.')
