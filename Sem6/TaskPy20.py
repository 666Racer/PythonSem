# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# def ListInput (n):
#     array = []
#     num = 0
#     while (num < n):
#         number = int(input(f"Вводите {num1+1}-й элемент массива: "))
#         array.append(number)
#         num +=1
#     return array

list_1 = []
n = int(input('Введите количество элементов N в массиве: '))
num1 = 0
while (num1 < n):
    number = int(input(f"Вводите {num1+1}-й элемент массива: "))
    list_1.append(number)
    num1 +=1
print(list_1)

def SearchElemWithLessNeighbours (array):
    count = 0
    for i in range(1,len(array)-1):
        if array[i-1] < array[i] and array[i+1] < array[i]:
            count +=1
    return count

print(f"Количество элементов, 2 соседних элемента котрого меньше него, равно {SearchElemWithLessNeighbours (list_1)}")

# n = int(input('Введите кол-во элементов множества -> '))
# arr = [input('Введите элемент массива -> ') for i in range(0, n)]
# res = [1 for i in range(0,len(arr)) if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]]
# print(sum(res))