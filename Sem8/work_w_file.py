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


def choose(choice):
    if choice == '1': return write(input("Введите ваши данные (пример: фамилия имя отчество номер телефона)"))
    if choice == '2': return read_all()
    if choice == '3': return get_by_name(input("Введите имя или фамилию"))
    if choice == '-1': exit()

# https://github.com/OlgaMigal/Python2023.git
# Seminar8



                