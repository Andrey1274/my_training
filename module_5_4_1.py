class House: #=> создаем класс House

    houses_history = [] #=> определяем пустой список внутри класса House

    def __new__(cls, *args, **kwargs): #=> определяем метод __new__ внутри класса House
        cls.houses_history.append(args[0]) #=> добавляем название объекта в созданный список внутри класса House
        return object.__new__(cls) #=> возвращаем объект с обновленным методом __new__ в класс House

    def __init__(self, name, number_of_floors): #=> определяем метод (с созданием объекта) __init__ внутри класса House
        self.name = name #=> передаем атрибут (имя) объекта внутри метода __init__
        self.number_of_floors = number_of_floors #=> передаем атрибут (количество этажей) объекта внутри метода __init__

    def go_to(self, new_floor): #=> определяем метод go_to внутри класса House
        if 1 <= new_floor <= self.number_of_floors: #=> проверяем условие, чтобы параметр new_floor был не меньше 1 и не более number_of_floors
            for i in range(1, new_floor + 1): #=> запуск цикла
                print(i) #=> вывод на консоль номера этажа i
        else: #=> иначе
            print('Такого этажа не существует') #=> вывод на консоль сообщения, если не выполняется условие

    def __len__(self): #=> определяем специальный метод __len__ внутри класса House
        return self.number_of_floors #=> возвращаем значение атрибута number_of_floors (количества этажей)

    def __str__(self): #=> определяем специальный метод __str__ внутри класса House
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}' #=> возвращаем значение атрибутов (name) и (number_of_floors)

    def __eq__(self, other): #=> определяем специальный метод __eq__(==) внутри класса House
        return self.number_of_floors == other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __lt__(self, other): #=> определяем специальный метод __lt__(<) внутри класса House
        return self.number_of_floors < other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __le__(self, other): #=> определяем специальный метод __le__(<=) внутри класса House
        return self.number_of_floors <= other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __gt__(self, other): #=> определяем специальный метод __gt__(>) внутри класса House
        return self.number_of_floors > other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __ge__(self, other): #=> определяем специальный метод __ge__(>=) внутри класса House
        return self.number_of_floors >= other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __ne__(self, other): #=> определяем специальный метод __ne__(!=) внутри класса House
        return self.number_of_floors != other.number_of_floors #=> возвращаем результат сравнения значений атрибутов False или True

    def __add__(self, value): #=> определяем специальный метод __add__ внутри класса House, который позволяет добавлять переданное значение value
        if isinstance(value, int): #=> проверяем тип переданного значения value на принадлежность к целым числам (int)
            self.number_of_floors += value #=> добавляется переданное значение value к значению атрибута number_of_floors (количества этажей)
            return self #=> возвращаем значение самого объекта

# Специальные методы: __radd__(self, value) и __iadd__(self, value) работают так же как и метод __add__(self, value)
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __del__(self): #=> определяем специальный метод __del__ внутри класса House
        if hasattr(self, 'manually_deleted') and self.manually_deleted: #=> проверяется условие, что явно вызывается del для удаления объекта (наличие атрибута на удаление)
            print(f'Дом в {self.name} снесён, но он останется в истории')
        else:
            pass #=> пустой оператор

h1 = House('ЖК Эльбрус', 10) #=> задаем объект h1
print(House.houses_history)
h2 = House('ЖК Акация', 20) #=> задаем объект h2
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20) #=> задаем объект h3
print(House.houses_history)

# Удаление объектов
#h1.manually_deleted = True #=> установление специального атрибута на удаление объекта h1
h2.manually_deleted = True #=> установление специального атрибута на удаление объекта h2
h3.manually_deleted = True #=> установление специального атрибута на удаление объекта h3
del h1 #=> вызываем метод __del__ для объекта h1
del h2 #=> вызываем метод __del__ для объекта h2
del h3 #=> вызываем метод __del__ для объекта h3
print(House.houses_history)

#go_to
#h1.go_to(5) #=> вызываем метод go_to для объекта h1
#h2.go_to(10) #=> вызываем метод go_to для объекта h2

#__str__
#print(h1) #=> вывод на консоль значения объекта h1
#print(h2) #=> вывод на консоль значения объекта h2

#__len__
#print(len(h1)) #=> вывод на консоль результата метода __len__ по объекту h1
#print(len(h2)) #=> вывод на консоль результата метода __len__ по объекту h2

# __eq__
#print(h1 == h2) #=> вывод на консоль результата сравнения False или True

# __add__
#h1 = h1 + 10
#print(h1) #=> вывод на консоль значения объекта h1
#print(h1 == h2) #=> вывод на консоль результата сравнения False или True

# __iadd__
#h1 += 10
#print(h1) #=> вывод на консоль значения объекта h1

# __radd__
#h2 = 10 + h2
#print(h2) #=> вывод на консоль значения объекта h2

# __gt__(>)
#print(h1 > h2) #=> вывод на консоль результата сравнения False или True

# __ge__(>=)
#print(h1 >= h2) #=> вывод на консоль результата сравнения False или True

# __lt__(<)
#print(h1 < h2) #=> вывод на консоль результата сравнения False или True

# __le__(<=)
#print(h1 <= h2) #=> вывод на консоль результата сравнения False или True

# __ne__(!=)
#print(h1 != h2) #=> вывод на консоль результата сравнения False или True
