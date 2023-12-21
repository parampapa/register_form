import json


def validate(username, data):
    for i in data:
        if i.get('username') == username:
            return True
    return False


def register():
    while True:
        username = input('Введите логин: ')
        if len(username) < 3 or len(username) > 21:
            print('Некорректный логин. Логин должен содержать не менее 3 и не более 20 символов')
            continue
        if validate(username, data):
            print(f'Логин {username} уже используется')
        else:
            break

    while True:
        password = input('Введите свой пароль: ')
        if len(password) < 4 or len(password) > 31:
            print('Некорректный пароль. Пароль должен состоять не менее чем из 4 и не более чем из 30 символов')
            continue
        else:
            new_user = {'username': username, 'password': password}
            data.append(new_user)
            with open('Database.json', 'w', encoding='UTF-8') as file:
                json.dump(data, file)
            print('Вы успешно зарегистрированы!')
            break


def login(data):
    user_found = False
    name = input('Введите свой логин: ')
    for i in data:
        if name == i['username']:
            user_found = True
            password = input('Введите пароль: ')
            if i['password'] == password:
                print('Элвис вошел в здание!')
                break
            else:
                print('Неправильный пароль!')
    if not user_found:
        print('Нет такого логина!')


def pathway(data):
    path = input('Введите 1, чтобы войти,\n'
                 'Введите 2, чтобы зарегистрироваться:\n')
    try:
        if int(path) == 1:
            login(data)
        elif int(path) == 2:
            register()
        else:
            print('Вам нужно ввести либо "1", либо "2". Другие цифры не сработают.')
            pathway(data)
    except ValueError:
        pathway(data)


try:
    with open('Database.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    data = []

pathway(data)
