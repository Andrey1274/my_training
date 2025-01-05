# Импортируем необходимые модули
from datetime import datetime #=> ипортируем модуль работы с датой и временем
import multiprocessing #=> импортируем модуль многопроцессорного программирования


def read_info(name): #=> создаем функцию для чтения файлов
    all_data = [] #=> создаётся изначально пустой локальный список
    with open(name, encoding="utf-8") as file: #=> открывается файл с использованием раскодировки utf-8
        data = file.readline() #=> проводим считывание строки файла
        while data: #=> открываем цикл с условием (пока имеются строки в считываемом файле)
            data = file.readline() #=> проводим считывание строки файла
            all_data.append(data[0:-1]) #=> добавляем строку в список all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)] #=> создаём список имен файлов

#Линейный вызов
start = datetime.now() #=> в переменную start записываем текущее время
read_info(filenames[0]) #=> вызываем функцию read_info для считывания файла
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
end = datetime.now() #=> в переменную end записываем текущее время
print(f'Линейный вызов: {end - start}') #=> выводим на консоль время считывания файлов

# многопроцессный
if __name__ == '__main__': #=> используем конструкцию для кода без его импортирования в другой модуль
    start = datetime.now() #=> в переменную start записываем текущее время
    with multiprocessing.Pool(processes=4) as pool: #=> запускаем класс Pool, зпускающий процесс параллельного выполнения задач
        pool.map(read_info, filenames) #=> используем метод map для чтения файлов из списка filenames
    end = datetime.now() #=> в переменную end записываем текущее время
    print(f'Многопроцессный вызов: {end - start}') #=> выводим на консоль время считывания файлов