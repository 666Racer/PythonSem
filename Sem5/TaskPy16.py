# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# 1 2 3 4 5 5 5 5
# 1 2 3 4 1 1 1 1

def MaxSearch (array):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    return max

def MinSearch (array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
    return min

list_1 = [] #оформить как функцию?
n = int(input('Введите количество оценок Василия: '))
num1 = 0 #заполняем массив оценок
while (num1 < n):
    number = int(input("Вводите оценки Василия: "))
    if number >= 1:
        list_1.append(number)
        num1 +=1
    else:
        print("Введена неверная оценка, введите правильную!")
print(list_1) #вывод массива оценок до изменений

maximum = MaxSearch(list_1)
minimum = MinSearch(list_1)
for i in range(1, len(list_1)):
    if list_1[i] == maximum:
        list_1[i] = minimum
print(list_1) #вывод изменённого массива


# my_list = [1, 2, 3, 4, 5, 5, 5, 5]

# def min_max(my_list):
#     min = max = my_list[0]
#     for i in my_list:
#         if i>max:
#             max=i
#         if i<min:
#             min = i
#     return (min, max)

# # min, max = min_max(my_list)

# def change_min_max(my_list, temp):
#     for i in range(len(my_list)):
#         if my_list[i]==temp[1]:
#             my_list[i]=temp[0]
#     return my_list

# print (change_min_max(my_list, min_max(my_list)))

