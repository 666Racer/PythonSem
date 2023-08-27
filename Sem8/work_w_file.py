# Программа

def write(text): #add?
    with open ('file.txt', "a", encoding="utf-8") as f:
       f.writelines(text)
       f.writelines("\n")
       print("Данные были записаны")

def read_all():
    # if  "file.txt".exists("file.txt"):
        with open ('file.txt', "r", encoding="utf-8") as f:
            for line in f:
                print(line[:-1]) #делает срез, убирает лишнюю строку

def get_by_name(name):
    with open ('file.txt', "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print (line)

def delete_line (name):
    with open ('file.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open ('file.txt', "w", encoding="utf-8") as f:  
        for line in lines:
            if name not in line:
                f.write(line)
        print("Данные были удалены")

def change_line (old_tag, new_tag):
    with open ('file.txt', "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if old_tag in line:
                line = line.replace(old_tag, new_tag)
            f.write(line)
        print("Данные были изменены")


def choose(choice):
    if choice == '1': return write(input("Введите ваши данные (пример: фамилия имя отчество номер телефона): "))
    if choice == '2': return read_all()
    if choice == '3': return get_by_name(input("Введите имя или фамилию: "))
    if choice == '4': return delete_line(input("Введите имя или фамилию: "))
    if choice == '5': return change_line(input("Введите старый параметр (фамилия/имя/отчество/телефон) для замены: "), input("Введите новый параметр (фамилия/имя/отчество/телефон) для замены: "))
    if choice == '-1': exit()

# https://github.com/OlgaMigal/Python2023.git
# Seminar8



                