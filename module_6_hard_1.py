import math  #=> импортирование модуля math для математических операций, таких как вычисление площади и корня.

class Figure: #=> создаем родительский класс (Figure - фигура)
    sides_count = 0  #=> определяем атрибут (sides_count - количество сторон) класса Figure и присваиваем ему значение 0

    def __init__(self, color, *sides): #=> создаем метод создания объектов внутри класса Figure
        self.__sides = []  #=> определяем атрибут объекта внутри класса Figure (__sides - стороны)
                           # с двумя нижними подчеркиваниями (инкапсулированный) как пустой список
        self.__color = list(color)  #=> определяем атрибут объекта внутри класса Figure (__color - цвет фигуры)
                                    # с двумя нижними подчеркиваниями (инкапсулированный) (номер цвета в формате RGB) в виде списка
        self.filled = False  #=> определяем атрибут (публичный) объекта внутри класса Figure (filled - закрашенный)
                             # и присваиваем ему значение False

        if not self.__is_valid_sides(*sides):  #=> делаем проверку на количество переданных сторон
            self.__sides = [1] * self.sides_count  #=> в случае выполнения условия, создаем массив с единичными сторонами
                                                   # и в том количестве, которое требует фигура
        else:
            self.__sides = list(sides)  #=> иначе, сохраняем переданный список сторон

    def __is_valid_color(self, r, g, b): #=> создаем метод __is_valid_color внутри класса Figure
                                         # для проверки корректности переданных значений цвета
        return all(isinstance(x, int) and 0 <= x <= 255 for x in(r, g, b))  #=> проверяем, что все значения - целые числа
                                                                            # в диапазоне от 0 до 255

    def set_color(self, r, g, b): #=> создаем метод set_color внутри класса Figure для изменения цвета
        # Устанавливает новый цвет, если он корректный:
        if self.__is_valid_color(r, g, b):  #=> проверяем корректность цвета, запуская метод __is_valid_color
            self.__color = [r, g, b]  #=> переопределяем атрибут списка цветов
        # Если цвет некорректный, ничего не меняем

    def get_color(self): #=> создаем метод get_color внутри класса Figure для возвращения списка RGB цветов
        return self.__color  #=> возвращает текущий список RGB цветов

    def __is_valid_sides(self, *new_sides): #=> создаем метод __is_valid_sides внутри класса Figure
                                            # для проверки корректности переданного количества сторон
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)
        #=> проверяем количество сторон в соответствующей фигуре и что все стороны - положительные целые числа

    def get_sides(self): #=> создаем метод get_sides внутри класса Figure для возвращения списка сторон фигуры
        return self.__sides  #=> возвращает список сторон фигуры

    def set_sides(self, *new_sides): #=> создаем метод set_sides внутри класса Figure для изменения количества сторон
        if self.__is_valid_sides(*new_sides):  #=> gроверяем корректность новых сторон, запуская метод __is_valid_sides
            self.__sides = list(new_sides)  #=> переопределяем атрибут списка сторон

    def __len__(self): #=> применяем магический метод для подсчета периметра фигуры
        return sum(self.__sides)  #=> возвращает сумму всех сторон (периметр)


class Circle(Figure): #=> создаем дочерний класс (Circle - окружность)
    sides_count = 1  #=> определяем атрибут (sides_count - количество сторон) класса Circle
                     # и присваиваем ему значение 1 т.к. у круга одна сторона

    def __init__(self, color, circumference): #=> создаем метод создания объектов внутри класса Circle,
                                              # с атрибутами объекта: color - цвет, circumference - длина окружности
        super().__init__(color)  #=> вызываем конструктор родительского класса Figure

        if not isinstance(circumference, (int, float)) or circumference <= 0:  #=> проверяем тип и значение окружности
            raise ValueError("Circumference must be a positive number.")  #=> объявляем ошибку при некорректном значении

        self.__radius = circumference / (2 * math.pi)  #=> рассчёт радиуса по длине окружности
        self.set_sides(circumference)  #=> устанавливаем длину окружности как сторону

    def get_square(self): #=> создаем метод get_square внутри класса Circle для расчета площади круга
        return math.pi * (self.__radius ** 2)  #=> возвращаем площадь круга: π * r^2


class Triangle(Figure): #=> создаем дочерний класс (Triangle - треугольник)
    sides_count = 3  #=> определяем атрибут (sides_count - количество сторон) класса Triangle
                     # и присваиваем ему значение 3

    def __init__(self, color, a, b, c): #=> создаем метод создания объектов внутри класса Triangle,
        super().__init__(color, a, b, c)  #=> вызываем конструктор родительского класса Figure с тремя сторонами

    def get_square(self): #=> создаем метод get_square внутри класса Triangle для расчета площади
                          # треугольника (по формуле Герона)
        a, b, c = self.get_sides()  # Получаем стороны треугольника

        if not all(isinstance(side, (int, float)) and side > 0 for side in (a, b, c)): #=> проверяем на корректность задание сторон треугольника
            raise ValueError("All sides must be positive numbers.")  #=> объявляем ошибку если стороны треугольника заданы некорректно

        s = (a + b + c) / 2  #=> расчет полупериметра
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  #=> расчет площади треугольника через полупериметр по формуле Герона


class Cube(Figure): #=> создаем дочерний класс (Cube - куб)
    sides_count = 12  #=> определяем атрибут (sides_count - количество сторон) класса Cube
                      # и присваиваем ему значение 12 (количество рёбер у куба)

    def __init__(self, color, edge_length): #=> создаем метод создания объектов внутри класса Cube
        super().__init__(color)  #=> вызываем конструктор родительского класса Figure

        if not isinstance(edge_length, (int, float)) or edge_length <= 0: #=> проверяем на корректность заданное значение длины ребра
            raise ValueError("Edge length must be a positive number.") #=> объявляем ошибку если длина ребра куба задана некорректно

        self.set_sides(*[edge_length] * self.sides_count) #=> здесь список сторон многоугольника
                                                          # состоит из 12 равных значений (рёбер куба)

    def get_volume(self): #=> создаем метод get_square внутри класса Cube для расчета объема
        edge_length = self.get_sides()[0]  #=> длина ребра куба равна длине любой стороны т.к. все стороны одинаковы
        return edge_length ** 3  #=> возвращаем объём куба: a^3


# Пример использования классов
circle1 = Circle((200, 200, 100), 10)  #=> создаем объект круга с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  #=> создаем объект куба с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  #=> изменение цвета круга
print(circle1.get_color())  #=> выводим текущий цвет круга: [55,66,77]
cube1.set_color(300, 70, 15)  #=> попытка изменить цвет куба на некорректный
print(cube1.get_color())  #=> выводим текущий цвет куба: [222,35,130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12)  #=> попытка изменить стороны куба на некорректные
print(cube1.get_sides())  #=> выводим текущие стороны куба: [6]*12
circle1.set_sides(15)  #=> изменение стороны круга на новую длину окружности
print(circle1.get_sides())  #=> выводим текущие стороны круга: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  #=> выводим длину окружности: ~15.71

# Проверка объёма (куба):
print(cube1.get_volume())  #=> выводим объём куба: ~216