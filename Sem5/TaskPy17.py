# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

# 1
# 2
# 3
# 4
# 5

# func(5)

# 5 4 3 2 1

def Reverse(num):
    if num == 0:
        return ""
    number = input("Введите число: ")
    return f"{Reverse(num-1)}{number} " #пробел в конце, потому что идём в обратную сторону
    

n = int(input("Введите число N элементов: "))
print(Reverse(n))
