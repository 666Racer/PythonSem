# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите {i+1}-й элемент списка из {x} элементов: ")))
    return my_list

def Search_Indexes_Of_Elems_In_Range (min, max, array):
    array_of_indexes = []
    for i in range(len(array)):
        if array[i] >= min and array[i] <= max:
            array_of_indexes.append(i)
    return array_of_indexes


n = int(input('Введите количество элементов в массиве: '))
list_1 = list_creator(n)

minimum = int(input('Введите минимальный элемент диапазона: '))
maximum = int(input('Введите максимальный элемент диапазона: '))
list_of_indexes = Search_Indexes_Of_Elems_In_Range (minimum, maximum, list_1)
print(f"Индексы элементов, лежащих в диапазоне от {minimum} до {maximum} - {list_of_indexes}")