# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

# import os

from alghoritm import *
from work_w_file import *

while True:
    # os.system('cls' if os.name == 'nt' else 'clear')

    print_instructions()
    choose(input("Введите команду 1, 2, 3 или -1"))
    input("Введите enter чтобы продолжить")
# clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
# clear()