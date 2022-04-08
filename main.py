from datetime import datetime


def Outp():
    infile = open('output.txt', 'a+', encoding="utf-8")
    admin = open('users.txt', 'r+', encoding='utf-8')
    i = input('\nВведите логин и пароль через пробел: ').split()
    if len(i) > 1:
        for line in admin:
            f = line.split()
            if i[0] == f[0] and i[1] == f[1]:
                infile.write(
                    'Пользователь' + ' ' + f[0] + ' успешно авторизовался' + ' ' + str(datetime.today())[:19] + '\n')
                i[1] = True
                if f[2] == 'True':
                    i.append('True')
                else:
                    i.append('False')
                print(i)
                break

    elif len(i) != 2:
        infile.write('Неверное имя пользователя или пароль:' + ' ' + i[0] + ' ' + str(datetime.today())[:19] + '\n')
        i = ['guest', False, 'False']
    admin.close()
    infile.close()
    return i


def Cnk():
    user = Outp()
    if 'admin' in user[0] and user[1] == True:
        print('Приветствую пользователя:' + user[0], '\n', '1)Просмотреть файл логов', '\n',
              '2)Посмотреть список пользователей', '\n', '3)Изменить пароль у Пользователя \n',
              '4)Добавить пользователя \n', '5)Удалить пользователя \n', '6)Заблокировать пользователя\n',
              '7)Разблокировать пользователя\n', '8)Выход\n')
        i = int(input())
        while i != 8:
            if i == 1:
                print('//-------------------------------------\\' + '\\')
                [print(i, end='') for i in open('output.txt', encoding='utf-8')]
                print('//_____________________________________\\' + '\\')
                open('output.txt', 'a+', encoding='utf-8').write(
                    'Администратор посмотрел логи' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 2:
                print('*----------------------------*')
                [print(i, end='') for i in open('users.txt', encoding='utf-8')]
                print('\n*____________________________*')
                open('output.txt', 'a+', encoding='utf-8').write(
                    'Администратор посмотрел список пользователей' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 3:
                us = input('Введите имя пользователя: ')
                cache = open('users.txt', 'r', encoding='utf-8').read().split()
                open('users.txt', 'w').close()  # clear file
                for i in range(len(cache)):  # search on target word
                    if cache[i] == us:
                        passw = input(
                            'В пароле должна содержаться кириллица,латиница и цифра\n' + 'Введите пароль на каторый хотите изменить: ')
                        if mask(passw):
                            cache[i + 1] = passw
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Пароль у пользователя ' + us + ' успешно изменён' + ' ' + str(datetime.today())[
                                                                                           :19] + '\n')

                            break
                        else:
                            print('Пароль не подходит для требований\n')
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Не удалось изменить пароль у пользователя ' + us + ' ' + str(datetime.today())[
                                                                                          :19] + '\n')
                            break
                f = open('users.txt', 'w', encoding='utf-8')
                for i in range(0, len(cache), 3):  # write in file from the cache
                    f.write(cache[i] + ' ' + cache[i + 1] + ' ' + cache[i + 2] + '\n')

                f.close()

            elif i == 4:
                name = input('Введите логин: ')
                passw = input(
                    'Введите пароль\nПароль должен содеражать кириллицу,латинницу,цифру и быть длинной более 7 символов\n')
                if mask(passw):
                    open('users.txt', 'a+', encoding="utf-8").write(name +
                                                                    ' ' + passw + ' ' + 'True' + '\n')
                    open('output.txt', 'a+', encoding='utf-8').write(
                        'Пользователь ' + name + ' успешно добавлен' + ' ' + str(datetime.today())[:19] + '\n')
                else:
                    print('Пароль не допустим.\nВозвращение в меню')
                    open('output.txt', 'a+', encoding='utf-8').write(
                        'Пользователь ' + name + ' не добавлен' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 5:
                us = input('Введите имя пользователя: ')
                cache = open('users.txt', 'r', encoding='utf-8').read().split()
                open('users.txt', 'w').close()  # clear file
                for i in range(len(cache)):  # search on target word
                    if cache[i] == us:
                        del cache[i]
                        del cache[i]
                        del cache[i]
                        open('output.txt', 'a+', encoding='utf-8').write(
                            'Пользователь ' + us + ' успешно удалён' + ' ' + str(datetime.today())[:19] + '\n')
                        break
                f = open('users.txt', 'w')
                for i in range(0, len(cache), 3):  # write in file from the cache
                    f.write(cache[i] + ' ' + cache[i + 1] + ' ' + cache[i + 2] + '\n')

                f.close()
            elif i == 6 or i == 7:
                if i == 6:
                    user = input('Введите имя пользователя, для блокировки доступа\n')
                if i == 7:
                    user = input('Введите имя пользователя, для разблокировки доступа\n')
                cache = open('users.txt', 'r', encoding='utf-8').read().split()
                open('users.txt', 'w').close()  # clear file
                for j in range(len(cache)):
                    if cache[j] == user:
                        if i == 6:
                            cache[j + 2] = 'False'
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Администратор заблокировал пользователя ' + user + ' ' + str(datetime.today())[
                                                                                          :19] + '\n')
                            print('Пользователь:', user, 'успешно заблокирован\n')
                            break
                        if i == 7:
                            cache[j + 2] = 'True'
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Администратор разблокировал пользователя ' + user + ' ' + str(datetime.today())[
                                                                                           :19] + '\n')
                            print('Пользователь:', user, 'успешно разблокирован\n')
                            break

                f = open('users.txt', 'w', encoding='utf-8')
                for j in range(0, len(cache), 3):  # write in file from the cache
                    f.write(cache[j] + ' ' + cache[j + 1] + ' ' + cache[j + 2] + '\n')

                f.close()

            i = int(input('1)Просмотреть файл логов\n' +
                          '2)Посмотреть список пользователей\n' + '3)Изменить пароль у Пользователя\n' +
                          '4)Добавить пользователя \n' + '5)Удалить пользователя \n' + '6)Заблокировать пользователя\n' + '7)Разблокировать пользователя\n' + '8)Выход\n'))
    elif user[0] != 'guest' and user[1] == True and len(user) > 1 and user[2] == 'True':
        print('Вы вошли как обычный пользователь :' + user[0] + '\n', '1)Изменить свой пароль\n', '2)Выйти\n')
        i = int(input())
        while i == 1:
            cache = open('users.txt', 'r', encoding='utf-8').read().split()
            open('users.txt', 'w').close()  # clear file
            for i in range(len(cache)):
                if user[0] == cache[i]:  # search on target word
                    passw = input(
                        'В пароле должна содержаться кириллица,латиница и цифра\n' + 'Введите пароль на каторый хотите изменить: ')
                    if mask(passw):
                        cache[i + 1] = passw
                        open('output.txt', 'a+', encoding='utf-8').write(
                            'Пароль у пользователя ' + user[0] + ' успешно изменён' + ' ' + str(datetime.today())[
                                                                                            :19] + '\n')
                        break
                    else:
                        print('Пароль не подходит для требований\n')
                        open('output.txt', 'a+', encoding='utf-8').write(
                            'Не удалось изменить пароль у пользователя ' + user[0] + ' ' + str(datetime.today())[
                                                                                           :19] + '\n')
                        break
        f = open('users.txt', 'w', encoding='utf-8')
        for j in range(0, len(cache), 3):  # write in file from the cache
            f.write(cache[j] + ' ' + cache[j + 1] + ' ' + cache[j + 2] + '\n')

        f.close()

        i = int(input('1)Изменить свой пароль\n' + '2)Выйти\n'))

    elif user[0] != 'guest' and user[1] == True and len(user) > 1 and user[2] == 'False':
        print('Пользователь:', user[0], 'Заблокирован администратором\n', 'Меню программы:\n', '1)Авторизоваться\n',
              '2)Выход\n')
        i = int(input())

    else:
        print('\nТы не авторизовался, у тебя нет прав!', 'Возвращение в меню.', '\nМеню программы:', '1)Авторизоваться',
              '2)Выход', sep='\n')
        open('output.txt', 'a+', encoding='utf-8').write(
            'Неверный логин или пароль' + ' ' + str(datetime.today())[:19] + '\n')
        i = int(input())

    return i


def mask(passw):
    a = 0
    k = list('ёйцукенгшщзхъфывапролджэячсмитьбю')
    l = list('qwertyuiopasdfghjklzxcvbnm')
    m = list('1234567890')
    for i in k:
        if i in passw.lower():
            a += 1
            break
    for i in l:
        if i in passw.lower():
            a += 1
            break
    for i in m:
        if i in passw:
            a += 1
            break
    if a == 3 and len(passw) >= 8:
        return True
    else:
        return False


def menu():
    print('Меню программы:', '1)Авторизоваться', '2)Выход', sep='\n')
    i = int(input())
    while i == 1:
        i = Cnk()



menu()
