calls = 0 #=> создаем переменную calls для подсчета количества вызовов функций (string_info и is_contains) и присваиваем ей значение ноль
def count_cals (): #=> объявляем функцию count_cals для изменения переменной calls
    global calls #=> переменную calls делаем глобальной в данной функции count_cals
    calls += 1 #=> добавляем единицу к переменной calls при каждом запуске функции count_cals
def string_info (string): #=> объявляем функцию string_info с одним строковым параметром
    count_cals() #=> запускаем функцию count_cals
    return (len(string), string.upper(), string.lower()) #=> создаем кортеж из длины строки (количество символов), строки в верхнем регистре и строки в нижнем регистре и завершаем выполнение функции
def is_contains (string, list_to_search): #=> объявляем функцию is_contains с двумя параметрами (строка и список)
    count_cals() #=> запускаем функцию count_cals
    return string.upper() in [d.upper() for d in list_to_search] #=> проверяем, находится ли заданная строка (string) в заданном списке (list_to_search). Все элементы строки и списка переводим при этом в нижний регистр
print(string_info('Capybara')) #=> запуск функции string_info с выводом результата на консоль
print(string_info('Armageddon')) #=> запуск функции string_info с выврдом результата на консоль
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) #=> запуск функции is_contains с выврдом результата на консоль
print(is_contains('cycle', ['recycling', 'cyclic'])) #=> запуск функции is_contains с выврдом результата на консоль
print(calls) #=> вывод количества вызовов функций (string_info и is_contains)