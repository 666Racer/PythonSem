# 3) Дан список целых чисел, оставить в нём только двузначные числа

list_1 = [1, -13, -2, 45, -100, 664, 56]

num_array = list(filter(lambda x: 10 <= abs(x) <= 99, list_1))
print(num_array)