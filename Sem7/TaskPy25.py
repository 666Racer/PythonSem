# 1) Дан список, вывести в отдельном списке буквы, а в другом цифры, используя фильтр.

# ["asd", 1, 2, "gfd"]
# ["asd", "gfd"][1,2]

# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(input(f"Введите {i+1}-й элемент списка из {x} элементов: ")))
#     return my_list

# n = int(input('Введите количество элементов в массиве: '))
# list_1 = list_creator(n)

list_1 = ["asd", 1, 2, "gfd"]

num_array = list(filter(lambda x: type(x) == int, list_1))
print(num_array)

string_array = list(filter(lambda x: type(x) == str, list_1))
print(string_array)

