# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# list_1 = [1,0,4,-1,-5,0,8,4,1]
# count = 0
# min_value = list_1[0]
# for i in list_1:
#     if i+1 > min_value:
#         count +=1
#     i +=1
# print(f"Количество элементов, больших предыдущего, равно {count}")

spisok = [4, 3, 5, 6, 1, 2]
chislo = [[spisok[i-1], spisok[i]] for i in range(1, len(spisok)) if spisok[i] > spisok[i-1]]
chislo2 = [print(' (' + str(item[0]) + ' < ' + str(item[1]) + ') ') for item in chislo]
