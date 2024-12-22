from random import choice #=> вызываем функцию choice из модуля random

# Lambda-функция:
first = 'Мама мыла раму' #=> первая заданная строка по условию задачи
second = 'Рамена мало было' #=> вторая заданная строка по условию задачи
res = list(map(lambda x, y: x == y, first, second)) #=> в пременную res создаём список (list), в который будет сохраняться
                                                    # результат сравнения букв из заданных строк, с помощью обработки этих
                                                    # строк встроенной функцией map и Lambda-функцией
print(res) #=> вывод на консоль


# Замыкание:
def get_advanced_writer(file_name): #=> объявляем функцию get_advanced_writer с аргументом file_name,
                                    # принимающим имя файла для записи
    def write_everything(*data_set): #=> объявляем функцию write_everything с аргументом, принимающим неограниченное
                                     # количество данных любого типа
        with open(file_name, "w", encoding='UTF-8') as file: #=> открываем файл для перезаписи с раскодировкой 'UTF-8'
            for element in data_set: #=> открываем цикл для перебора значений из аргумента data_set
                file.write(str(element) + '\n') #=> перезаписываем файл с новой строки
    return write_everything #=> возвращаем функцию write_everything

write = get_advanced_writer('example.txt') #=> запускаем функцию высшего порядка: get_advanced_writer, которая будет
                                           # возвращать нам вложенную функцию write_everything и сохранять её в переменную write
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке']) #=> запускаем вложенную функцию write_everything
                                                                              # через переменную write


# Метод __call__:
class MysticBall: #=> создаем класс MysticBall
    def __init__(self, *words: str): #=> определяем метод (с созданием объекта) __init__ внутри класса MysticBall
        self.words = words #=> передаем атрибут объектов words, хранящий коллекцию строк
    def __call__(self): #=> определяем метод __call__, который будет случайным образом выбирать слово из words и возвращать его
        return choice(self.words) #=>
first_ball = MysticBall('Да', 'Нет', 'Наверное') #=> запускаем объект класса MysticBall
print(first_ball()) #=> вывод объекта на консоль
print(first_ball())
print(first_ball())