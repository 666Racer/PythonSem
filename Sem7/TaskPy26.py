# 2) Дано вещественное число, показать сумму его цифр.

num = float(input('Введите вещественное число: '))
# num_str = str(num)
# splitted = num_str.replace(".", "")
# result = sum(map(lambda x: int(x), splitted)) 
# print(f"Сумма цифр в вещественном числе {num} равна {result}")


# result = sum(list(map(lambda x: int(x), str(num).replace(".", ""))))
# print(f"Сумма чисел в числе {num} равна {result}")
print(f'Сумма чисел в числе {num} равна {sum(list(map(lambda x: int(x), str(num).replace(".", ""))))}')

# num = 3.12
# stroka = str(num)

# res = list(filter(lambda x: x != ".", stroka))
# res = sum(list(map(int, res)))