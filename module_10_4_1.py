# Задача "Потоки гостей в кафе"
# Импортируем необходимые модули
import random #=> импортируем модуль генерации случайных чисел
from threading import Thread #=> импортируем класс создания потоков из модуля потоков
from time import sleep #=> импортируем функцию sleep для из модуля time для создания временных пауз между действиями
from queue import Queue #=> импортируем класс Queue из модуля queue для работы с очередью

# Создаём класс Table - стол, где будет хранится информация о находящемся за ним гостем (Guest).
class Table():
    def __init__(self, number): #=> создаем метод создания объектов внутри класса Table с атрибутами: number и guest
        self.number = number
        self.guest = None #=> изначальное значение атрибута None

# Создаём дочерний класс Guest - гость, который наследуется от класса Thread (Поток)
class Guest(Thread):
    def __init__(self, name): #=> создаем метод создания объектов внутри класса Guest с атрибутом: name
        super().__init__() #=> передаем атрибуты объектов родительского класса Thread в дочерний класс Guest
        self.name = name

    def run(self): #=> создаем метод run для организации случайной паузы (от 3-х до 10 секунд)
        # sleep(random.randint(3, 10))
        pause =  random.randint(3, 10)
        sleep(pause)

# Создаём класс Cafe - кафе, в котором есть определённое кол-во столов
# и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests)
class Cafe:
    list_thr = [] #=> создаем изначально пустой список потоков по обслуживанию

    def __init__(self, *tables): #=> создаем метод создания объектов внутри класса Cafe с атрибутами: queue и tables
        self.queue = Queue() #=> атрибут queue (очередь)
        self.tables = list(tables) #=> атрибут tables здесь прописывается как список (list) столов

    def guest_arrival(self, *guests): #=> создаем метод guest_arrival (прибытие гостей)
        list_guests = list(guests) #=> вводим переменную со списком гостей
        list_tables = self.tables #=> вводим переменную со списком столов
        len_list_guests = len(list_guests) #=> вводим переменную с количеством гостей
        min_guests_tables = min(len_list_guests, len(self.tables)) #=> вводим переменную для определения минимального количества гостей
        for i in range(min_guests_tables): #=> открываем цикл для перебора столов
            list_tables[i].guest = guests[i] #=> назначаем каждому столу гостя
            thr1 = guests[i] #=> открываем поток по обслуживанию i-того гостя
            thr1.start()  #=> запускаем поток thr1
            Cafe.list_thr.append(thr1) #=> добавляем в список потоков поток thr1
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')
        if len_list_guests > min_guests_tables: #=> проверяем условие: если количество гостей больше минимального количества гостей за столами
            for i in range(min_guests_tables, len_list_guests): #=> открываем цикл для перебора гостей, оставшихся без столов
                self.queue.put(guests[i]) #=> добавляем гостя в очередь
                print(f'{list_guests[i].name} в очереди')

    def discuss_guests(self): #=> создаём метод, имитирующий обслуживание гостей
        while not (self.queue.empty()) or Cafe.check_table(self): #=> открываем цикл с условиями: пока очередь не пустая
                                                                  # или хотя бы один стол занят
            for table in self.tables: #=> открываем цикл для перебора столов
                if not (table.guest is None) and not (table.guest.is_alive()): #=> проверяем условие: если за столом нет гостя
                                                                               # и гость закончил прием пищи (поток закрыт)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None: #=> проверяем условие, если очередь еще не пуста и за столом нет гостя
                    table.guest = self.queue.get() #=> берём гостя из очереди
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr1 = table.guest #=> открываем поток (обслуживание гостя)
                    thr1.start() #=> запускаем поток
                    Cafe.list_thr.append(thr1) #=> добавляем в список потоков поток thr1

    def check_table(self): #=> создаём метод определения статуса стола
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


# Создание списка столов
tables = [Table(number) for number in range(1, 6)]
# Список имен гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание списка гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
# cafe.guest_arrival(*guests)
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
for thr in Cafe.list_thr:
    thr.join()