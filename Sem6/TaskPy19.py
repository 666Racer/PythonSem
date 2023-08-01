# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

list_1 = []
n = int(input('Введите количество элементов N в первом массиве: '))
num1 = 0
while (num1 < n):
    number = int(input("Вводите элементы первого массива: "))
    list_1.append(number)
    num1 +=1
print(list_1)

list_2 = []
m = int(input('Введите количество элементов M во втором массиве: '))
num2 = 0
while (num2 < m):
    number = int(input("Вводите элементы второго массива: "))
    list_2.append(number)
    num2 +=1
print(list_2)

def SearchElem (array1, array2):
    array = []
    for i in array1:
        if i not in array2:
            array.append(array1[i])
    return array

print(SearchElem (list_1, list_2))

# def task039():
#     m = int(input("Введите длину списка m: "))
#     n = int(input("Введите длину списка n: "))
#     list_m = list_creator(m)
#     list_n =list_creator(n)
#     res_list = set_from_list(list_m, list_n)
#     print(*res_list)

# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
#     return my_list

# def set_from_list(list_m, list_n):
#     my_list = [list_m[i] for i in range(len(list_m)) if list_m[i] not in list_n]
#     return my_list

# task039()