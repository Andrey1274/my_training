# Импортирование необходимых модулей
from threading import Thread #=> импортирование модуля создания потоков
from time import sleep


class Knight(Thread): #=> создаём дочерний класс Knight

    def __init__(self, name: str, power: int): #=> создаем метод создания объектов внутри класса Knight с атрибутами: name, power
        super().__init__() #=> прописываем все атрибуты родительского класса Thread в дочерний класс Knight
        self.name = name #=> определяем атрибут объекта внутри класса Knight (name - имя рыцаря)
        self.power = power #=> определяем атрибут объекта внутри класса Knight (power - сила рыцаря)
        self.enemies = 100 #=> определяем атрибут объекта внутри класса Knight (enemies - изначальное число врагов у рыцаря)
        self.days = 0 #=> определяем атрибут объекта внутри класса Knight (enemies - изначальное количество дней сражения рыцаря)

    def run(self):
        print(f'{self.name}, на нас напали!') #=> вывод на консоль сообщения от рыцаря

        while self.enemies > 0: #=> открываем цикл с условием
            self.days += 1 #=> подсчет количества дней
            self.enemies -= self.power #=> подсчет численности врагов у рыцаря
            sleep(1) #=> задержка по времени (1 секунда)

            print(f"{self.name} сражается {self.days} день(ей)..., осталось {self.enemies} воинов.") #=> вывод на консоль сообщения
        print(f"{self.name} одержал победу спустя {self.days} дней!") #=> вывод на консоль сообщения


if __name__ == '__main__': #=> запускаем конструкцию для проверки условия импортирования данного файла как модуля
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')