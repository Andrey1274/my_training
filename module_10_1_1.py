# Импортируем все необходимые модули
from time import sleep
from datetime import datetime
from threading import Thread

# Объявление функции write_words, согласно задания
def write_words(word_count, file_name): #=> здесь параметр word_count - это количество перезаписываемых слов,
                                        #=> file_name - название файла, куда будут перезаписываться слова
    file = open(file_name, 'a', encoding='utf-8') #=> открываем файл с раскодировкой utf-8 для добавления (перезаписи) в него слов
    for i in range(word_count): #=> открываем цикл для перезаписи слов в этот файл
        file.write( f'Какое-то слово №  {i+1}\n') #=> перезаписываем (добавляем) новое слово в файл
        sleep(0.1) #=> устанавливаем задержку перезаписи в 0,1 секунду
    file.close() #=> закрываем наш файл
    print(f'Завершилась запись в файл {file_name}') #=> вывод на консоль сообщения о завершении процесса записи в файл

# Взятие текущего времени
time_start = datetime.now() #=> старт счетчика времени

# Запуск функций с аргументами из задачи
# После создания файла вызовите 4 раза функцию wite_words
write_words(10, 'example1.txt') #=> запуск функции write_words с заданными параметрами word_count и file_name
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now() #=> стоп счетчика времени
time_result = time_stop - time_start #=> расчет потраченного времени на выполнение последовательной перезаписи 4-х файлов

# Вывод разницы начала и конца работы функций
print(f'Время работы функций {time_result}') #=> вывод на консоль

# После вызовов функций создайте 4 потока для вызова этой функции
"""Здесь будем каждый файл перезаписывать в отдельном потоке, т.е. перезапись всех 4-х файлов будет вестись параллельно"""
# Взятие текущего времени
time2_start = datetime.now() #=> старт счетчика времени

# Создание и запуск потоков с аргументами из задачи
thread_first = Thread(target=write_words, args= (10, 'example5.txt')) #=> создаём поток thread_first с параметрами:
                                                                      # target - принимает на вход нашу функцию write_words
                                                                      # для перезаписи файлов
                                                                      # args - принимает на вход аргументы функции write_words
thread_second = Thread(target=write_words, args= (30, 'example6.txt'))
thread_third = Thread(target=write_words, args= (200, 'example7.txt'))
thread_fourth = Thread(target=write_words, args= (100, 'example8.txt'))

thread_first.start() #=> запуск первого потока
thread_second.start() #=> запуск второго потока
thread_third.start() #=> запуск третьего потока
thread_fourth.start() #=> запуск четвертого потока

# Остановка основного потока.
thread_first.join()
thread_second.join()
thread_third.join()
thread_fourth.join()

# Взятие текущего времени

time2_stop = datetime.now() #=>стоп счетчика времени
time2_result = time2_stop - time2_start #=> расчет потраченного времени на выполнение параллельной перезаписи 4-х файлов
print(f'Время работы потоков {time2_result}') #=> вывод на консоль

# Вывод разницы времени работы потоков
print(f'Использование Потоков быстрее функций на {time_result-time2_result} секунд')