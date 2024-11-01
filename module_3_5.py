def get_multiplied_digits(number): #=> объявляем функцию (get_multiplied_digits) с одним параметром (number)
    str_number = str(number) #=> переводим заданное число (number) в строку (str_number)
    first = int(str_number[0]) #=> извлекаем первый символ из строки (str_number) и преводим его в целое число

    if len(str_number) > 1: #=> проверяем условие, чтобы количество символов в строке (str_number) было больше 1
        return first * get_multiplied_digits(int(str_number[1:])) #=> прерывание и запуск функции (get_multiplied_digits)
    else: #=>
        return first #=> прерывание и возврат оставшейся цифры (first)


result = get_multiplied_digits(40203) #=> запись результата
print(result) #=> вывод результата на консоль