def calculate_structure_sum(data_structure): #=> объявляем функцию для подсчёта данных строк и чисел с параметрами из условия задачи

    summa = 0 #=> определяем переменную (сюда будем вести подсчет) с начальным значением ноль

    if isinstance(data_structure, dict): #=> определяем условие: если аргумент переменной (data_structure) является словарем
        for key, value in data_structure.items(): #=> запускаем цикл для перебора всех пар ключ-значение (key-value) в словаре с помощью метода (items())
            summa += calculate_structure_sum(key) #=> вызываем фукцию для подсчета ключей из словаря
            summa += calculate_structure_sum(value) #=> вызываем функцию для подсчета значений из словаря

    elif isinstance(data_structure, (list, tuple, set)): #=> определяем условие: если аргумент переменной (data_structure) является списком (list), кортежем (tuple) или множеством (set)
        for item in data_structure: #=> запускаем цикл для перебора всех аргуметов в списке, кортеже или множестве
            summa += calculate_structure_sum(item) #=> вызываем функцию для подсчета аргументов из списка, кортежа или множества

    elif isinstance(data_structure, (int, float)): #=> определяем условие: если аргумент переменной (data_structure) является числом (целым или вещественным)
        summa += data_structure #=> к переменной (summa) добавляется значение числа из переменной (data_structure)

    elif isinstance(data_structure, str): #=> определяем условие: если аргумент переменной (data_structure) является строкой (str)
        summa += len(data_structure) #> к переменной (summa) добавляется количество символов строки

    return summa #=> прерывание функции и возвращение результата её работы

#=> Данные из условия задачи, в виде переменной (data_structure):
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

#=> Выводим результаты работы программы:
result = calculate_structure_sum(data_structure) #=> результат работы функции (calculate_structure_sum) записывается в переменную (result)
print(result) #=> вывод значения переменной (result) на консоль