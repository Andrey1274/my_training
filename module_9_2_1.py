first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable'] #=> первый заданный список
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'] #=> второй заданный список

# В переменную first_result записывается список, созданный при помощи сборки, состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов:
first_result = [len(first_string) for first_string in first_strings if len(first_string) >= 5]

# В переменную second_result записывается список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
second_result = [(first_string, second_string) for first_string in first_strings for second_string in second_strings
                 if len(first_string) == len(second_string)]

# В переменную third_result записывается словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки
third_strings = first_strings + second_strings #=> объединяем в один список два заданных списка

third_result = {third_string: len(third_string) for third_string in third_strings if len(third_string) % 2 == 0}

print(first_result) #=> выводим результаты на консоль
print(second_result)
print(third_result)