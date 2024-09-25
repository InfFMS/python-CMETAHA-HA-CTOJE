# Задача 10: Уравнение прямой
# Напишите программу, которая находит значение y в уравнении прямой y = kx + b для заданных x, k и b.
# Пример:
# Ввод: k = 2, b = 3, x = 5
# Вывод: y = 13
# вводить стоит, как пример "k = 2, b = 3, x = 5"
nums_input = input('>>> ')
nums = nums_input.split(', ')
index_int = []
list_k = nums[0]
index_int.append(int(list_k[-1]))
list_x = nums[1]
index_int.append(int(list_x[-1]))
list_b = nums[2]
index_int.append(int(list_b[-1]))
print(f'y = {index_int[0] * index_int[1] + index_int[2]}')
