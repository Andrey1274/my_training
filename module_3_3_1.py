# №1 Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'string_s', c = True): #=> объявляем функцию print_params с именованными параметрами, т.е. параметрами по умолчанию
    print(a, b, c) #=>  вывод на консоль параметров функции

print_params() #=> вызов функции без аргументов
print_params(5, 'text', False)  #=> вызов функции print_params с тремя аргументами
print_params(112, 'waterfall')  #=> вызов функции print_params с двумя аргументами + 1 по умолчанию
print_params(b = 'exam') #=> вызов функции print_params с одним аргументом + 2 по умолчанию
print_params(b = 25) #=> вызов функции print_params с одним измененным именным параметром
print_params(c = [1, 2, 3]) #=> вызов функции print_params с одним измененным именным параметром
print('')

# №2 Распаковка параметров:
values_list = [458, 'string_data', False] #=> создание списка с тремя элементами разных типов
values_dict = {'a': 50, 'b': 'table', 'c': True} #=> создание словаря, соответствующими параметрам функции print_params, и значениями разных типов
print_params(*values_list) #=> вызов функции print_params с распаковкой списка (* для списка)
print_params(**values_dict) #=> вызов функции print_params с распаковкой словаря (** для словаря)
print('')
# Одновременно передать values_list и values_dict в функцию print_params невозможно,
# не изменив количество элементов

# №3 Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка'] #=> создание списка с двумя элементами разных типов
print_params(*values_list_2, 42) #=> вызов функции print_params с распаковкой списка и добавлением аргумента